import urllib.request
import json
from .models import Sources

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


def get_articles(name):
    get_articles_url = "https://newsapi.org/v2/everything?q=name&from=2021-08-12&sortBy=popularity&apiKey=360b4d3017ff40d6ac61fd173e189625"
    with urllib.request.urlopen(get_articles_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)

        article_object = None

        if article_response['articles']:
            at_result_list = article_response["articles"]
            at_results = process_articles(at_result_list)
    return at_results


def process_articles(article_list):
    article_results = []
    for article in article_list:
        author =author.get("author")
        title = article.get("title")
        description = article.get("description")
        urlToImage = article.get("urlToImage")
        url = article.get("url")
        publishedAt = article.get("publishedAt")

        article_object = Sources(
            title, description, urlToImage, url, publishedAt)
        article_results.append(article_object)

    return article_results

    


def get_sources(name):
    get_articles_details_url = article_url.format(api_key)

    with urllib.request.urlopen(get_articles_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            title = news_details_response.get("title")
            description = news_details_response.get("description")
            urlToImage = news_details_response.get("urlToImage")
            url = news_details_response.get("url")
            publishedAt = news_details_response.get("publishedAt")

            news_object = Sources(
                title, description, url, urlToImage, publishedAt)
    return news_object
