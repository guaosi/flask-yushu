from flask import Flask,make_response
app=Flask(__name__)
app.config.from_object('config')
@app.route('/hello')
def hello():
    headers={
        'content-type':'text/plain',
        'content-type':'application',
        'content-type':'text/html',
        'location':'http://www.baidu.com'
    }
    response=make_response('<html></html>',404)
    response.headers=headers
    return response
    # return 'Hello,guaosi1'
    # return '<html></html>',301,headers
#app.add_url_rule('/hello',view_func=hello)
if __name__=='__main__':
    app.run(host=app.config['HOST'] , port=app.config['PORT'] , debug=app.config['DEBUG'])