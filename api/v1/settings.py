from v1.films import films
from v1.users import users

DOMAIN = {
    'users' : users,
    'films' : films,
}

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
MONGO_USERNAME = '<your username>'
MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'apitest'