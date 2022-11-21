from flask import Flask
from flask_restful import Resource, Api
from classes.movie import movie
from classes.links import links
from classes.ratings import ratings
from classes.tags import tags

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class getMovie(Resource):
    def get(self):
        list = []

        f = open("data/movies.csv", "r", encoding='utf8')
        f.readline()
        for x in f:
            z = x.rstrip('\n').split(',')  # Do poprawy split by ignorował przecinki w cudzysłowiach
            list.append(movie(z[0], z[1], z[2]).__dict__)
        f.close()
        return list


class getLinks(Resource):
    def get(self):
        list = []

        f = open("data/links.csv", "r", encoding='utf8')
        f.readline()
        for x in f:
            z = x.rstrip('\n').split(',')  # Do poprawy split by ignorował przecinki w cudzysłowiach
            list.append(links(z[0], z[1], z[2]).__dict__)
        f.close()
        return list


class getRatings(Resource):
    def get(self):
        list = []

        f = open("data/ratings.csv", "r", encoding='utf8')
        f.readline()
        for x in f:
            z = x.rstrip('\n').split(',')  # Do poprawy split by ignorował przecinki w cudzysłowiach
            list.append(ratings(z[0], z[1], z[2], z[3]).__dict__)
        f.close()
        return list


class getTags(Resource):
    def get(self):
        list = []

        f = open("data/tags.csv", "r", encoding='utf8')
        f.readline()
        for x in f:
            z = x.rstrip('\n').split(',')  # Do poprawy split by ignorował przecinki w cudzysłowiach
            list.append(tags(z[0], z[1], z[2], z[3]).__dict__)
        f.close()
        return list


api.add_resource(HelloWorld, '/')
api.add_resource(getMovie, '/movies')
api.add_resource(getLinks, '/links')
api.add_resource(getRatings, '/ratings')
api.add_resource(getTags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
