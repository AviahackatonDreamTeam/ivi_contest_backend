def post_get_callback(resource, request, payload):
    print('A GET on the "%s" endpoint was just performed!' % resource)

def post_films_get_callback(request, payload):
    print('A get on "films" was just performed!')