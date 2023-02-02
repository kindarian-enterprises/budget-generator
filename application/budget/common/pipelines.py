def make_pagination_pipeline(offset, page_size, filters):
    '''
    Args:
        offset (int): The offset of objects that should be
            skipped in the pipeline.
        page_size (int): The ammount of objects per page that
            will be returned.
        filters (dict): A dictionary of filters that will be
            matched during the aggregation

    Returns:
        list: A list of objects outlining the aggregation steps
            to be taken.
    '''
    mongo_pipeline = [
        {"$match":filters},
        {
            "$sort": {
                "dateCreated": -1
            }
        },
        {"$skip": offset},
        {"$limit": page_size},
        {
            "$project": {
                "date": {
                    "$dateToString": {
                        "date": "$dateCreated",
                        "format": "%Y-%m-%d",
                    },
                },
                "goal": 1,
                "_id": 0
                }
        }
    ]
    return mongo_pipeline
