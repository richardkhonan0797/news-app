import os

from ..models.news import NewsModel
from newsapi import NewsApiClient

api_key=os.getenv('NEWS_API_KEY')
newsapi = NewsApiClient(api_key=api_key)

updating = False

countries = [
    'id',
    'us',
    'cn',
    'hk',
    'ph',
    'sg',
    'my'
]

categories = [
    'general',
    'business', 
    'technology', 
    'science', 
    'health', 
    'sports', 
    'entertainment'
]

def fetch_new_news():
    updating = True
    for country in countries:
        for category in categories:
            NewsModel.delete_by_country_and_category(country, category)
            top_headlines = newsapi.get_top_headlines(
                                                        category=category,
                                                        country=country)
            news_list = [ News(
                    source_id= key['source']['id'], 
                    source_name = key['source']['name'],
                    author = key['author'],
                    title = key['title'],
                    description = key['description'],
                    url = key['url'],
                    urlToImage = key['urlToImage'],
                    publishedAt = key['publishedAt'],
                    content = key['content'],
                    country = country,
                    category = category
                ) for key in top_headlines['articles']]

            NewsModel.save_all_to_db(news_list)
    updating = False


