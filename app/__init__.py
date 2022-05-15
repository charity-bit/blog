from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_login import LoginManager
from flask_ckeditor import CKEditor



db = SQLAlchemy()
bootstrap = Bootstrap()
ckeditor = CKEditor()



login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


photos = UploadSet('photos',IMAGES)

def create_app(config_name):

    
    app = Flask(__name__)


    app.config.from_object(config_options[config_name])
    configure_uploads(app,photos)
    app.config['UPLOADED_PHOTOS_DEST'] = 'app/static/photos'

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)

    
    from app.requests import configure_request
    configure_request(app)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

   
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
     

   


    return app
