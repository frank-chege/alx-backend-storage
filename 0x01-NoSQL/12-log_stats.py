#!/usr/bin/env python3
'''show some nginx stats'''
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db  = client['logs']
nginx = db['nginx'] #collection

def count_no(kwargs):
    '''counts the records in the db'''
    count = db.nginx.count_documents(kwargs)
    return count

def main():
    '''show some nginx stats'''
    print(count_no({}), 'logs')
    print(f"Methods:\n\
    method GET: {count_no({'method': 'GET'})}\n\
    method POST: {count_no({'method': 'POST'})}\n\
    method PUT: {count_no({'method': 'PUT'})}\n\
    method PATCH: {count_no({'method': 'PATCH'})}\n\
    method DELETE: {count_no({'method': 'DELETE'})}")
    print(count_no({'path': '/status'}), 'status check')

if __name__ == '__main__':
    main()