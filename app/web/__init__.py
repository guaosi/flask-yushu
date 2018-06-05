#蓝图初始化操作
from flask import Blueprint
web=Blueprint('web',__name__)
from . import book