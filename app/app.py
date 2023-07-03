from flask import Flask
from flask_pymongo import PyMongo
from config import DATABASE_URI

app = Flask(__name__)
app.config['MONGO_URI'] = DATABASE_URI
mongo = PyMongo(app)
collection = mongo.db.record_ingestion



