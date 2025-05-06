import requests
from django.conf import settings

# Fetch from The Guardian
def fetch_guardian(query):
    url = "https://content.guardianapis.com/search"
    params = {
        'api-key': settings.GUARDIAN_KEY,
        'q': query,
        'show-fields': 'headline,trailText,thumbnail,short-url'
    }
    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    if 'response' in data and 'results' in data['response']:
        for item in data['response']['results']:
            articles.append({
                'title': item['webTitle'],
                'content': item['fields'].get('trailText', 'No content available.'),
                'url': item['webUrl'],
                'image_url': item['fields'].get('thumbnail', '')
            })
    return articles

# Fetch from New York Times
def fetch_nyt(query):
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params = {
        'q': query,
        'api-key': settings.NYT_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    if 'response' in data and 'docs' in data['response']:
        for item in data['response']['docs']:
            image_url = ""
            if item.get('multimedia'):
                for media in item['multimedia']:
                    if media.get('subtype') == 'thumbnail':
                        image_url = f"https://www.nytimes.com/{media['url']}"
                        break

            articles.append({
                'title': item.get('headline', {}).get('main', 'No Title'),
                'content': item.get('lead_paragraph', 'No content available.'),
                'url': item.get('web_url', '#'),
                'image_url': image_url
            })
    return articles

# Fetch from NewsAPI
def fetch_newsapi(query):
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': query,
        'apiKey': settings.NEWS_API_KEY,
        'language': 'en'
    }
    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    if 'articles' in data:
        for item in data['articles']:
            articles.append({
                'title': item.get('title', 'No Title'),
                'content': item.get('description', 'No content available.'),
                'url': item.get('url', '#'),
                'image_url': item.get('urlToImage', '')
            })
    return articles

# Fetch from GNews API
def fetch_gnews(query):
    url = "https://gnews.io/api/v4/search"
    params = {
        'q': query,
        'token': settings.GNEWS_KEY,
        'lang': 'en'
    }
    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    if 'articles' in data:
        for item in data['articles']:
            articles.append({
                'title': item.get('title', 'No Title'),
                'content': item.get('description', 'No content available.'),
                'url': item.get('url', '#'),
                'image_url': item.get('image', '')
            })
    return articles

# Fetch from MediaStack API
def fetch_mediastack(query):
    url = "http://api.mediastack.com/v1/news"
    params = {
        'access_key': settings.MEDIASTACK_KEY,
        'keywords': query,
        'languages': 'en'
    }
    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    if 'data' in data:
        for item in data['data']:
            articles.append({
                'title': item.get('title', 'No Title'),
                'content': item.get('description', 'No content available.'),
                'url': item.get('url', '#'),
                'image_url': item.get('image', '')
            })
    return articles

# Combine all fetchers
def fetch_all_articles(query):
    guardian_articles = fetch_guardian(query)
    nyt_articles = fetch_nyt(query)
    newsapi_articles = fetch_newsapi(query)
    gnews_articles = fetch_gnews(query)
    mediastack_articles = fetch_mediastack(query)

    all_articles = guardian_articles + nyt_articles + newsapi_articles + gnews_articles + mediastack_articles
    return all_articles
