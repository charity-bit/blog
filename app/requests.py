from urllib.request import urlopen
import json


RANDOM_QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quote():
    '''
      function that consumes storm quotes api to return random apis
    '''

    with urlopen(RANDOM_QUOTES_URL) as response:
        body = response.read()


    random_quote = json.loads(body)

    return random_quote

   
    

    

