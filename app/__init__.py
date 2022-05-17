from fileinput import filename
import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask,send_from_directory,request, url_for
from config import config_options
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_login import LoginManager
from flask_ckeditor import CKEditor,upload_success,upload_fail




basedir = os.path.abspath(os.path.dirname(__file__))


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


    app.config['CKEDITOR_SERVE_LOCAL'] = True
    app.config['CKEDITOR_HEIGHT'] = 400
    app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
    app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')


    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)

    
  
    
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

        
    @app.route('/files/<filename>')
    def uploaded_files(filename):
        path = app.config['UPLOADED_PATH']
        return send_from_directory(path,filename)

    @app.route('/upload',methods=['POST'])
    
    def upload():
        f = request.files.get('upload')
        extension =f.filename.split('.')[-1].lower()
        if extension not in ['jpg', 'gif', 'png', 'jpeg']:
            return upload_fail(message='Only Image Uploads allowed!')

        f.save(os.path.join(app.config['UPLOADED_PATH'],f.filename))
        url = url_for('uploaded_files',filename=f.filename)
        return upload_success(url,filename=f.filename)



    return app
