from Functions import loadImage as lI
from VideoFunctions import PlayVideo as pv
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_page():
    return 'Witaj w api. Wpisz /(photo lub video)/(folder)/(plik)'

@app.route('/photo/<folder>/<link>', methods=['GET', 'POST'])
def photo(folder,link):
    lI.load(folder+"/"+link)
    return "Zakończono przetwarzanie"

@app.route('/video/<folder>/<link>', methods=['GET', 'POST'])
def video(folder,link):
    pv.load(folder+"/"+link)
    return "Zakończono przetwarzanie"

if __name__ == '__main__':
    app.run()


