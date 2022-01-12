from pymongo import MongoClient
import os
from dotenv import load_dotenv
import certifi
load_dotenv()

mongopwd = os.getenv('MONGOPWD')
client = MongoClient("mongodb+srv://sak1sham:{}@cluster0.azvu4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(mongopwd), tlsCAFile=certifi.where())
db = client.todo_app
collection_name = db["todos_app"]