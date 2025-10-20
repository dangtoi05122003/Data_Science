from pymongo import MongoClient
from Database import MONGO_URI, MONGO_COLLECTION_VnExpress, MONGO_DB_VnExpress, MONGO_COLLECTION, MONGO_DB
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class connect():
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.database()
    def database(self):
        db = self.client[MONGO_DB]
        self.collection = db[MONGO_COLLECTION]
        db_VnExpress = self.client[MONGO_DB_VnExpress]
        self.collection_VnExpress = db_VnExpress[MONGO_COLLECTION_VnExpress]
    def load_data(self):
        return list(self.collection.find({}, {"_id": 0}))
    def load_data_VnExpress(self):
        return list(self.collection_VnExpress.find({}, {"_id": 0}))