from . import login_manager
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    username = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150),unique=True)
    pic_path = db.Column(db.String(255),default='avtar.png')
    date_joined = db.Column(db.DateTime(timezone = True),default = func.now())
    posts = db.relationship('Post',backref = 'user',passive_deletes = True)
    comments = db.relationship('Comment',backref = 'user',passive_deletes = True)
    upvotes = db.relationship('UpVote',backref = 'user',passive_deletes = True)
    downvotes = db.relationship('DownVote',backref = 'user',passive_deletes = True)


    def save_user(self):
        db.session.add(self)
        db.session.commit()


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.Text,nullable = False)
    pic_path = db.Column(db.String(255))
    date_created = db.Column(db.DateTime(timezone = True),default = func.now())
    author = db.Column(db.Integer,db.ForeignKey('users.id',ondelete="CASCADE"),nullable = False)
    comments = db.relationship('Comment',backref = 'post',passive_deletes = True)
    upvotes = db.relationship('UpVote',backref = 'post',passive_deletes = True)
    downvotes = db.relationship('DownVote',backref = 'post',passive_deletes = True)

    def save_post(self):
        db.session.add(self)
        db.session.commit()


    

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.String(200),nullable = False)
    date_created = db.Column(db.DateTime(timezone = True),default = func.now())
    author = db.Column(db.Integer,db.ForeignKey('users.id',ondelete="CASCADE"),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id',ondelete="CASCADE"),nullable = False)
    


class UpVote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.Integer,db.ForeignKey('users.id',ondelete="CASCADE"),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id',ondelete="CASCADE"),nullable = False)
    


class DownVote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.Integer,db.ForeignKey('users.id',ondelete="CASCADE"),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id',ondelete="CASCADE"),nullable = False)
    

class Quote:
    def __init__(self,id,author,quote,url):
        self.id  = id,
        self.author = author
        self.quote = quote
        self.url = url



   

    

    
