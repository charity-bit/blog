from . import db

from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    username = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150),unique=True)
    date_joined = db.Column(db.DateTime(timezone = True),default = func.now())
    posts = db.relationship('Post',backref = 'user',passive_deletes = True)
    comments = db.relationship('Comment',backref = 'user',passive_deletes = True)
    upvotes = db.relationship('UpVote',backref = 'user',passive_deletes = True)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.Text,nullable = False)
    date_created = db.Column(db.DateTime(timezone = True),default = func.now())
    author = db.Column(db.Integer,db.ForeignKey('users.id',ondelete="CASCADE"),nullable = False)


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.String(200),nullable = False)
    date_created = db.Column(db.DateTime(timezone = True),default = func.now())
    author = db.Column(db.Integer,db.ForeignKey('users.id',ondelete="CASCADE"),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id',ondelete="CASCADE"),nullable = False)
    comments = db.relationship('Comment',backref = 'post',passive_deletes = True)
    upvotes = db.relationship('UpVote',backref = 'post',passive_deletes = True)
    


class UpVote(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.Integer,db.ForeignKey('users.id',ondelete="CASCADE"),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id',ondelete="CASCADE"),nullable = False)
    date_created = db.Column(db.DateTime(timezone = True),default = func.now())


class DownVote(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.Integer,db.ForeignKey('users.id',ondelete="CASCADE"),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id',ondelete="CASCADE"),nullable = False)
    date_created = db.Column(db.DateTime(timezone = True),default = func.now())

    



   

    

    
