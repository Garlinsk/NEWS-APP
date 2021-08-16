from flask import render_template
from . import main
from ..requests import get_articles, news

@main.route("/")
def index():
    # top_news=news
    # print(top_news)
    sources=news()
    return render_template("index.html",sources=sources)

@main.route("/article")
def body():
    articles=get_articles()
    # bbc=get_articles("abc-news")
    # abc=get_articles("abc-news-au")
    # aljezera=get_articles("al-jazeera-english")
    # technica=get_articles("ars-technica")

    return render_template("articles.html",articles=articles)