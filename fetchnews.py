from sqlalchemy import MetaData, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from newsapi import NewsApiClient

metadata = MetaData()
Base = declarative_base(metadata=metadata)
engine = create_engine('postgres://aordjafm:xaBTfKgCsuriQvOLb0gLItqGC2GzGutH@drona.db.elephantsql.com:5432/aordjafm')
session = Session(engine)

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key = True)
    source_id = Column(String)
    source_name = Column(String)
    author = Column(String)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    urlToImage = Column(String)
    publishedAt = Column(String)
    content = Column(String)
    country = Column(String)
    category = Column(String)


# metadata.create_all(engine)

newsapi = NewsApiClient(api_key='0d2e9ff8c3b34e0ebc75cdb5646af286')

def query(country, category):
    return session.query(News).filter_by(country=country,category=category).count()

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

def get_news_from_api():
    for country in countries:
        for category in categories:
            count = query(country, category) 
            if count == 0:
                print(count, 'NGEFETCH')
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

                session.add_all(news_list)
                session.commit()
                session.close()
            else:
                print(count, "NGGA NGEFETCH")

get_news_from_api()
