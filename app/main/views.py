from unicodedata import category
from flask_login import current_user

from app.models import Post
from . import main
from flask import render_template,redirect,request,url_for,flash
from .forms import PostForm

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add-post',methods = ['GET','POST'])
def add_post():
    user_id = current_user.id
    form =  PostForm()
    if request.method == 'POST':
        content = form.body.data
        title = form.title.data
        # check if user is admin
        if user_id != 1:
            flash('Sorry, You are not allowed to post in this site',category = 'error')
        else:
            if not content:
                flash('Content of the post cannot be empty',category = 'error')
            elif not title:
                flash('title of the article cannot be empty')
            else:
                new_post = Post(title = title, text = content,author = current_user.id)
                new_post.save_post()
                flash("Article published successfully",category = "success")
                return redirect(url_for('main.index'))


    return render_template('admin/addpost.html',form = form)
