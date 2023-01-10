from Functions import loadImage as lI
from VideoFunctions import PlayVideo as pv
#name1 = 'Photos/photo3.jpg'
#name2 = 'Photos/photo4.jpg'
#name3 = 'Videos/video5.mp4'
#name4 = 'Photos/photo5.jpg'
#name5 = 'Photos/photo6.jpg'

#lI.load(name1)
#lI.load(name2)
#lI.load(name4)
#lI.load(name5)

#pv.load('Videos/video2.mp4')
#pv.load('Videos/video3.mp4')
#pv.load('Videos/video4.mp4')
#pv.load(name3)

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index_page():
    return 'hellowworld'

@app.route('/welcome')
def welcome():
    return render_template('index.html', text = 'hellow')

@app.route('/eyeFromAbove', methods=['GET', 'POST'])
def eye_from_above():
    if request.method == 'POST':
        return "Ye the user entered data"
    elif request.method == 'GET':
        return  '''
            <!doctype html>
            <title>Enter address to view</title>
            <h1>Enter the address to get image of</h1>
            <form method=post enctype=multipart/form-data>
              <input type=text name=address value=address>
              <input type=text name=date value='2013-12-17'>
              <input type=submit value=Submit>
            </form>
            '''

if __name__ == '__main__':
    app.run()


