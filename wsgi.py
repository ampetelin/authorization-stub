from os import environ

from waitress import serve

from authorization_stub import app

serve(app, host=environ['HOST'], port=environ['PORT'])
