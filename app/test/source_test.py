
import unittest
from app.models import Source,Article

news_source = Source

new_article = Article

class testSource(unittest.TestCase):
    '''
    Tests article test and source classes
    '''
    def setUp(self):
        '''
        Initiallizing classes from both modules
        '''

        self.news_source = news_source
        self.news_article = new_article
    def test__init__(self):
        '''
        Testing the news source and news article class
        '''

        self.assertTrue(isinstance(self.news_source,Source))
        self.assertTrue(isinstance(self.news_article,Article))