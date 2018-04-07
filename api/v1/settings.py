from api.v1.films import films
from api.v1.users import users
from os import environ as env

DOMAIN = {
    'users' : users,
    'films' : films,
}

MONGO_HOST = '0.0.0.0'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
MONGO_USERNAME = 'ApiAdmin'
MONGO_PASSWORD = env['APP_MONGO_TOKEN']

MONGO_DBNAME = 'apitest'