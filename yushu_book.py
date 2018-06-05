from HTTP import HTTP
from flask import current_app

class YuShuBook:
    isbn_url="http://t.yushu.im/v2/book/isbn/{}"
    key_url="http://t.yushu.im/v2/book/search?q={}&start={}&count={}"
    @classmethod
    def isbnSearch(cls,word):
        url=cls.isbn_url.format(word)
        result=HTTP.get(url)
        return result
    @classmethod
    def keySearch(cls,word,page=1):
        url=cls.key_url.format(word,cls.summaryStart(page),current_app.config['PRE_PAGE'])
        result=HTTP.get(url)
        return result
    @staticmethod
    def summaryStart(page):
        return (page - 1) * current_app.config['PRE_PAGE']
