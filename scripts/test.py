import unittest
import unittest.mock
from followUsers import getArticle

class TestFollowUser(unittest.TestCase):

    def test_getArticle(self):
        producer = unittest.mock.Mock()
        title, image = getArticle("https://www.bbc.com/news/world-asia-45539120", producer=producer, language="en")

if __name__ == '__main__':
    unittest.main()
