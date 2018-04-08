# /films endpoint
films_schema = {
    'title' : {
        'type' : 'string',
        'minlength' : 1,
        'maxlength' : 30,
    },
    'preview_link' : {
        'type' : 'string',
    },
    'imdb_rating' : {
        'type' : 'float',
    },
    'ivi_id' : {
        'type' : 'integer',
    },
    'is_serial' : {
        'type' : 'boolean',
    },
    'tags' : {
        'type' : ['string','list'],
    },
    'origin_country' : {
        'type' : 'string',
    },
    'janre' : {
        'type' : ['string', 'list'],
    },
    'release_date' : {
        'type' : 'date',
    },
}

films = {
    'item_titile': 'films',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema' : films_schema,
}
