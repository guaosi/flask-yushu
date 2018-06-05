from flask import jsonify, Blueprint
from helper import isIsbnOrKey
from yushu_book import YuShuBook
from . import web
@web.route('/book/search/<q>/<page>')
def search(q,page):
    is_isbn_or_key=isIsbnOrKey(q)
    if is_isbn_or_key=='isbn':
        result = YuShuBook.isbnSearch(q)
    if is_isbn_or_key=='key':
        result = YuShuBook.keySearch(q)
    return jsonify(result) #将dict转为json输出