
import os

class Config:
    UPLOADED_PHOTOS_DEST = os.environ.get('UPLOADED_PHOTOS_DEST')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:qwertyip@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'my_key'
    UPLOADED_PHOTOS_DEST='app/static/photos'
    
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)
  

class DevConfig(Config):
    DEBUG = True


    

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    
}