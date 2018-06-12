class BookViewModel:
    def __init__(self,book):
        self.image=book['image']
        self.title=book['title']
        self.author='、'.join(book['author'])
        self.publisher=book['publisher']
        self.pages=book['pages'] or ''
        self.price=book['price']
        self.isbn=book['isbn']
        self.summary=book['summary'] or ''
        self.pubdate=book['pubdate']
        self.binding=book['binding']
    @property
    def itor(self):
        res=filter(lambda x:True if x else False,[self.author,self.publisher,self.price])
        return ' / '.join(res)
class BookCollection:
    text=0
    def __init__(self):
        self.total=0
        self.books=[]
        self.keyword=''
    def fill(self,yushuBook,keyword):
        self.total=yushuBook.total
        self.keyword=keyword
        self.books=[BookViewModel(book) for book in yushuBook.books]
class _BookViewModel:
    # 描述特征(类变量，实例变量)
    # 行为（方法）
    @classmethod
    def package_single(cls,keyword,data):
        result_data={
            'keyword':keyword,
            'total':0,
            'books':[]
        }
        if data:
            result_data['total']=1
            result_data['books']=[cls._cut_book_data(data)]
        return result_data
    @classmethod
    def package_collection(cls,keyword,data):
        result_data = {
            'keyword': keyword,
            'total': 0,
            'books': []
        }
        if data:
            result_data['total']=data['total']
            result_data['books']=[cls._cut_book_data(book) for book in data['books']]
        return result_data
    @classmethod
    def _cut_book_data(cls,data):
        process_data={
            "image":data['image'],
            'title':data['title'],
            'author':'、'.join(data['author']),
            'publisher':data['publisher'],
            'pages':data['pages'] or '',
            'price':data['price'],
            'summary':data['summary'] or ''
        }
        return process_data