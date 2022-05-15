from crypt import methods
from unicodedata import category
from flask_login import current_user

from app.models import Post
from . import main
from flask import render_template,redirect,request,url_for,flash
from .forms import PostForm

@main.route('/')
def index():

    
    recents = []  # query recent posts
    all = Post.query.all()
    rev = all[::-1]

    for i in range(3):
        recents.append(rev[i])
    
       
    
    return render_template('index.html',recents = recents,all = all)

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

@main.route('/posts/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html',post = post)

@main.route('/posts/delete/<int:id>')
def delete_post(id):
    post = Post.query.get_or_404(id)
    if post:
        pass

    else:
        flash("post cannot be found",category="error")
    return redirect(url_for('main.post',id=post.id))

@main.route('/posts/edit-post/<int:id>',methods = ['GET','POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    current_user_id = current_user.id
    form = PostForm()

    if request.method == 'POST':          
        if  current_user_id !=1:
            flash('You cannot edit this post',category="error")
        else:
            if post:
                post.title = form.title.data
                post.text = form.body.data 

                post.save_post()

                flash("Post has been updated successfully",category="success")

                return redirect(url_for('main.post',id=post.id))
    
            else:
                flash('Post cannot be found',category="error")

    return render_template('admin/editpost.html',form = form)
