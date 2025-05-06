from .models import NewsArticle, Feedback
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_news(user_profile):
    preferred_categories = (getattr(user_profile, 'preferred_categories', '') or '').lower().split(',')
    preferred_categories = [cat.strip() for cat in preferred_categories if cat.strip()]

    all_articles = NewsArticle.objects.all()

    if not all_articles:
        return []

    # Try to filter matching articles
    matching_articles = []
    for article in all_articles:
        text = (article.title + " " + article.content).lower()
        if any(topic in text for topic in preferred_categories):
            matching_articles.append(article)

    # ⚡ If no matches, just pick random 10 articles and return
    if not matching_articles:
        fallback_articles = all_articles.order_by('?')[:10]  # random 10 articles
        return [{
            'title': article.title,
            'content': article.content,
            'url': article.url,
            'image_url': article.image_url,
        } for article in fallback_articles]

    # Otherwise, proceed with TF-IDF on matched articles
    articles_corpus = [article.title + " " + article.content for article in matching_articles]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(articles_corpus)

    user_pref_vector = vectorizer.transform([' '.join(preferred_categories)])

    cosine_similarities = cosine_similarity(user_pref_vector, tfidf_matrix).flatten()

    collaborative_scores = []
    for article in matching_articles:
        feedbacks = Feedback.objects.filter(article=article)
        if feedbacks.exists():
            avg_rating = np.mean([fb.rating for fb in feedbacks])
            collaborative_scores.append(avg_rating / 3)
        else:
            collaborative_scores.append(0.5)

    hybrid_scores = 0.7 * cosine_similarities + 0.3 * np.array(collaborative_scores)
    scored_articles = list(zip(matching_articles, hybrid_scores))
    sorted_articles = sorted(scored_articles, key=lambda x: x[1], reverse=True)

    recommended_articles = [{
        'title': article.title,
        'content': article.content,
        'url': article.url,
        'image_url': article.image_url,
    } for article, score in sorted_articles[:10]]

    return recommended_articles
