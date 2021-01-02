from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 

app = Flask("!Trash REST API") 
api = Api(app) 

def update_data(data):
    pass

class Analytics(Resource): 
    def get(self, category):
        if category is None or category == "":
            return jsonify([{"R": 0, "O": 0, "L": 0}])
        elif category.lower() == "r":
            return jsonify([{"R": 0, "O": 0, "L": 0}])
        elif category.lower() == "o":
            return jsonify([{"R": 0, "O": 0, "L": 0}])
        elif category.lower() == 'l':
            return jsonify([{"R": 0, "O": 0, "L": 0}]) 

    def post(self):
        data = request.get_json()
        update_data(data)
        return jsonify({'Message': "Success"}), 201

api.add_resource(Analytics, '/analytics/<str:category>') 


if __name__ == '__main__': 
	app.run(debug = True) 

