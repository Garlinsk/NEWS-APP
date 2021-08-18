from flask import render_template
from . import main
from ..requests import get_articles, get_sources

@main.route("/")
def index():
    articles=get_articles()

    return render_template("index.html",articles=articles)
    

@main.route("/sources")
def body():
   sources=get_sources()
   return render_template("sources.html",sources=sources)