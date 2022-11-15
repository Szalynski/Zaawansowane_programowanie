from flask import Flask
from flask_restful import Resource, Api
import re
from classes.movie import movie

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class getMovie(Resource):
    def get(self):
        list = []

        f = open("data/movies.csv", "r", encoding='utf8')
        print(f.readline())
        for x in f:
            z = x.split(',')
            list.append(movie(z[0], z[1], z[2]))

        f.close()
        return dir(list)


api.add_resource(HelloWorld, '/')
api.add_resource(getMovie, '/movies')

if __name__ == '__main__':
    app.run(debug=True)
