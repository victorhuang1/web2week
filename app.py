from flask import Flask
import json
from flask import render_template

app=Flask(__name__)

with open('/home/shiyanlou/files/helloshiyanlou.json','r') as file1:
    a=json.loads(file1.read())

with open('/home/shiyanlou/files/helloworld.json','r') as file2:
    b=json.loads(file2.read())

filename='/home/shiyanlou/news/templates/index.html'
with open(filename,'a') as file:
    file.write(a['title'])
    file.write(b['title'])

@app.route('/')
def index():
    return render_template('index.html')

#username WTF?

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__=='__main__':
    app.run(port=3000)
