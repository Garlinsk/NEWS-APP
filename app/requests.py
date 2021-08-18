import urllib.request
import json
from .models import Sources,Articles

api_key = None
base_url = None
source_url = None
article_url = None


def configure_request(app):
    global api_key, base_url, source_url, article_url
    api_key = app.config["NEWS_API_KEY"]
    base_url = app.config["NEWS_API_BASE_URL"]
    source_url = app.config["NEWS_BASE_URL"]
    article_url = app.config["NEWS_ARTICLE_API"]


def news():
    get_news_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=360b4d3017ff40d6ac61fd173e189625'
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_result_list = get_news_response['sources']
            news_results = process_results(news_result_list)

    return news_results


def process_results(news_list):
    news_results = []
    for news in news_list:

        id = news.get("id")
        name = news.get("name")
        description = news.get("description")
        category = news.get("category")
        url = news.get("url")

        if url:

            news_object = Sources(id, name, description, category, url)

            news_results.append(news_object)
    return news_results


'''
Fetching Articles
'''


def get_articles():
    get_articles_url = "https://newsapi.org/v2/everything?q=name&from=2021-08-12&sortBy=popularity&apiKey=360b4d3017ff40d6ac61fd173e189625"
    with urllib.request.urlopen(get_articles_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)

        article_results = None

        if article_response['articles']:
            article_result_list = article_response["articles"]
            article_results = process_articles(article_result_list)
    return article_results


def process_articles(article_list):
    article_results = []
    for article in article_list:
        author =article.get("author")
        title = article.get("title")
        description = article.get("description")
        urlToImage = article.get("urlToImage")
        url = article.get("url")
        publishedAt = article.get("publishedAt")

        article_object = Articles(
            title,author, description, urlToImage, url, publishedAt)
        article_results.append(article_object)

    return article_results

    


def get_sources():
    get_sources_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=360b4d3017ff40d6ac61fd173e189625'
    with urllib.request.urlopen(get_sources_url) as url:
        source_data = url.read()
        source_response = json.loads(source_data)

        source_results = None

        if source_response['sources']:
            source_result_list = source_response["sources"]
            source_results = process_sources(source_result_list)
    return source_results


def process_sources(source_list):
   source_results = []
   for source in source_list:
        id =source.get("id")
        name= source.get("name")
        description = source.get("description")
        url = source.get("url")
        category = source.get("category")

        source_object = Sources(
            id,name, description, url, category)
        source_results.append(source_object)

   return source_results


    # with urllib.request.urlopen(get_sources_url) as url:
    #     news_source_data = url.read()
    #     news_source_response = json.loads(news_source_data)

    #     news_source = None
    #     if news_source_response:
    #         title = news_source_response.get("title")
    #         description = news_source_response.get("description")
    #         urlToImage = news_source_response.get("urlToImage")
    #         url = news_source_response.get("url")
    #         publishedAt = news_source_response.get("publishedAt")

    #         news_object = Sources(
    #             title, description, url, urlToImage, publishedAt)
    # return news_object
