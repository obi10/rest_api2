import markdown
import os
import shelve #database

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)
# Create the API
api = Api(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("data_storage/data.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class DataList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        data = []

        for key in keys:
            data.append(shelf[key])

        return {'message': 'Success', 'data': data}, 200


    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id', required=True)
        parser.add_argument('num_personas', required=True)
        parser.add_argument('estado', required=True)
        parser.add_argument('tiempo', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['id']] = args

        return {'message': 'Data registered', 'data': args}, 201



class Data(Resource):
    def get(self, id):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (id in shelf):
            return {'message': 'Data not found', 'data': {}}, 404

        return {'message': 'Data found', 'data': shelf[id]}, 200

    def delete(self, id):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (id in shelf):
            return {'message': 'Data not found', 'data': {}}, 404

        del shelf[id]
        return '', 204


api.add_resource(DataList, '/data')
api.add_resource(Data, '/data/<string:id>')



