#!/usr/bin/env python

from bson.json_util import dumps
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("mongodb://localhost:27017/")
    db = client.<NOME_DA_BASE>
    collection = db.<NOME_DA_COLLECTION>
    cursor = collection.find({})
    with open('collection.txt', 'w') as file:              #SALVA A COLETA EM UM ARQUIVO TXT
        file.write('[')
        for document in cursor:
            file.write(dumps(document))
            file.write(',')
        file.write(']')
