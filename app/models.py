class News:
    def __init__(self,title,description,urlToImage,content,url):


        self.title=title
        self.description=description
        self.urlToImage=urlToImage
        self.content=content
        self.url=url
class Sources:
    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
class Articles:
    def __init__(self,title,description,url,urlToImage,publishedAt):
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
