import configparser
from pathlib import Path
import os

CONFIG_FILE = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)
        ),
        'appconfig.ini'
    )
APPCONFIG = configparser.ConfigParser()
APPCONFIG.read(CONFIG_FILE)

STATIC_DIR = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)
    ),
    '..',
    'static'
)

def make_mongo_pipeline(offset, page_size, filters):
    '''Takes in page data and return mongo aggregation
       pipeline query'''
    mongo_pipeline = [
      {"$match":filters},
      {"$skip": offset},
      {"$limit": page_size},
      {"$sort": {"dateCreated": -1}},
      { "$facet": {
            "data": [{
                "$group": {
                    "_id" : {
                        "$concat": [
                            {"$substr": [{"$dayOfMonth": "$dateCreated"}, 0, 2 ]},
                            "-",
                            {"$substr": [{"$month": "$dateCreated"}, 0, 2 ]},
                            "-",
                            {"$substr": [{"$year": "$dateCreated"}, 0, 4 ]},
                            "-",
                            {"$substr": [{"$second": "$dateCreated"}, 0, 3 ]},
                            "--",
                            {"$substr": [{"$abs": "$goal"}, 0, 10]},
                        ]
                    },
                }
            }],
        }
      }
    ]
    return mongo_pipeline
