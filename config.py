
import os

class Config:
    UPLOADED_PHOTOS_DEST = os.environ.get('UPLOADED_PHOTOS_DEST')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:qwertyip@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'my_key'
    UPLOADED_PHOTOS_DEST='app/static/photos'
    RANDOM_QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'


class ProdConfig(Config):
    pass
  

class DevConfig(Config):
    DEBUG = True


    

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    
}