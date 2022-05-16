import urllib.request
import json


RANDOM_QUOTES_URL = None


def configure_request(app):
    global RANDOM_QUOTES_URL
    RANDOM_QUOTES_URL = app.config['RANDOM_QUOTES_URL']


def get_quotes():

    '''
    function that fetches quotes

    '''
    quotes_url = RANDOM_QUOTES_URL
    with urllib.request.url(quotes_url) as url:
        data = url.read()
        response = json.loads(data)
        print(response)
        
        

    

