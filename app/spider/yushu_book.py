from app.lib.HTTP import HTTP
from flask import current_app

class YuShuBook:
    #类聚性
    isbn_url="http://t.yushu.im/v2/book/isbn/{}"
    key_url="http://t.yushu.im/v2/book/search?q={}&start={}&count={}"
    def __init__(self):
        self.books=[]
        self.total=0
    def isbnSearch(self,word):
        url=self.isbn_url.format(word)
        result=HTTP.get(url)
        self.__fill_single(result)
    def __fill_single(self,data):
        if data:
            self.total=1
            self.books=[data]

    def keySearch(self,word,page=1):
        url=self.key_url.format(word,self.summaryStart(page),current_app.config['PRE_PAGE'])
        result=HTTP.get(url)
        self.__fill_collection(result)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    def summaryStart(self,page):
        return (page - 1) * current_app.config['PRE_PAGE']
    @property
    def first(self):
        return self.books[0] if self.total != 0 else None