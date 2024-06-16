#!/usr/bin/env python3
'''This script is task 10's module.
'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a collection's
    document based on the name.
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
