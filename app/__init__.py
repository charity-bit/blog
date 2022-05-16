from flask_sqlalchemy import SQLAlchemy
import babel

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
     

    @app.template_filter()
    def format_date(value):
        months = ('January','February','March','April','May','June','July','August','September','October','November','December')
        month = months[value.month- 1]
        hour = str(value.hour).zfill(2)
        minutes = str(value.minute).zfill(2)
        #  posted June 22 2022 at 
        return "{} {} {} at {}:{}".format(month,value.day,value.year,hour,minutes)
   


    return app
