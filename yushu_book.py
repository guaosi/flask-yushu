from HTTP import HTTP


class YuShuBook:
    isbn_url="http://t.yushu.im/v2/book/isbn/{}"
    key_url="http://t.yushu.im/v2/book/search?q={}&start={}&count={}"
    @classmethod
    def isbnSearch(cls,word):
        url=cls.isbn_url.format(word)
        result=HTTP.get(url)
        return result
    @classmethod
    def keySearch(cls,word,start=0,count=15):
        url=cls.key_url.format(word,start,count)
        result=HTTP.get(url)
        return result

