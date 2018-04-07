# /users endpoint
users_schema = {
    'id' : {
        'type' : 'integer',
    },
    'fio' : {
        'type' : ['string', 'list']
    },
    'email' : {
        'type' : 'string',
    },
    'flights_history' : {
        'required' : False,
        'type': 'list',
        'schema' : {
            'type' : 'dict',
            'schema' : {
                'from' : {
                    'type' : 'string',
                },
                'to' : {
                    'type' : 'string',
                },
                'film' : {
                    'type':'list',
                    'schema' : {
                        'type' : 'integer', # ivi_id's of films viewed
                    }
                },
            },
        },
    }
}

users = {
    'item_titile': 'users',
    'resource_methods': ['GET', 'POST', 'PUT'],
    'schema' : users_schema,
}