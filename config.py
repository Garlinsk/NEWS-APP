import os
class Config:
    # "https://newsapi.org/v2/everything?q=Apple&from=2021-08-12&sortBy=popularity&apiKey=360b4d3017ff40d6ac61fd173e189625"
    NEWS_API_BASE_URL="https://newsapi.org/v2/top-headlines/sources?apiKey=360b4d3017ff40d6ac61fd173e189625"
    NEWS_BASE_URL="https://newsapi.org/v2/top-headlines/sources?apiKey={}"
    NEWS_ARTICLE_API="https://newsapi.org/v2/everything?q=popular&from=2021-08-12&sortBy=popularity&apiKey={}"
    NEWS_API_KEY=os.environ.get("NEWS_API_KEY")
    SECRET_KEY=os.environ.get("SECRET_KEY")


class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG=True

config_options={
"development":DevConfig,
"production":ProdConfig
}
