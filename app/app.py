# from flask import Flask, jsonify, request
# from flask_pymongo import PyMongo
# from config import DATABASE_URI

# app = Flask(__name__)
# app.config['MONGO_URI'] = DATABASE_URI
# mongo = PyMongo(app)
# collection = mongo.db.sample_data

# @app.route('/addResource', methods=['POST'])
# def add_resource():
#     payload = request.json
#     collection.insert_one(payload)
#     return jsonify("Added successfully")

# from flask import jsonify
# from bson import ObjectId  # Import the ObjectId class

# @app.route('/resource', methods=['GET'])
# def get_all_resource():
#     data = list(collection.find())
#     # Convert ObjectId to string for serialization
#     serialized_data = []
#     for item in data:
#         item['_id'] = str(item['_id'])
#         serialized_data.append(item)
#     return jsonify(data=serialized_data)


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from flask_pymongo import PyMongo
from config import DATABASE_URI

app = Flask(__name__)
app.config['MONGO_URI'] = DATABASE_URI
mongo = PyMongo(app)
collection = mongo.db.record_ingestion



