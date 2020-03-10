__author__ = "JrReubinJr"

from typing import Dict
import pymongo
import dns

class Database(object):
    path = "C:\Program Files\MongoDB\Server\MongoLogin.txt"
    file = open(path, 'r')
    uri = file.read()
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['pricing']

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query): #return first element return from cursor (json object)
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        return  Database.DATABASE[collection].remove(query)
