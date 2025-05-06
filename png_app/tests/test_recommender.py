import pytest
from png_app.models import NewsArticle, Feedback
from png_app.recommender import recommend_news

class DummyProfile:
    preferred_categories = 'technology, science'

@pytest.mark.django_db
def test_recommend_news_basic():
    NewsArticle.objects.create(
        title="New Advances in Science",
        content="Discussion of science discoveries",
        url="http://example.com/science",
        image_url="http://example.com/image1.jpg"
    )
    NewsArticle.objects.create(
        title="Cooking Tips",
        content="How to cook better",
        url="http://example.com/cooking",
        image_url="http://example.com/image2.jpg"
    )

    user_profile = DummyProfile()

    recommendations = recommend_news(user_profile)

    assert isinstance(recommendations, list)
    assert len(recommendations) > 0
    for article in recommendations:
        assert 'title' in article
        assert 'content' in article
        assert 'url' in article
        assert 'image_url' in article
