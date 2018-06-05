from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange


class SearchForm(Form):
    q=StringField(validators=[Length(min=1,max=30)]) #要与参数名称相同
    page=IntegerField(validators=[NumberRange(min=1,max=99)],default=1)  #要与参数名称相同