from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q=StringField(validators=[DataRequired(),Length(min=1,max=30)]) #要与参数名称相同，每个验证函数都可以自定义错误信息
    page=IntegerField(validators=[NumberRange(min=1,max=99)],default=1)  #要与参数名称相同