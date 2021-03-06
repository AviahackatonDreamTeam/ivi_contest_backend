from eve import Eve
from api.v1.settings import *
from api.v1.callbacks import post_get_callback, post_films_get_callback

app = Eve()

app.on_post_GET += post_get_callback
app.on_post_GET_films += post_films_get_callback