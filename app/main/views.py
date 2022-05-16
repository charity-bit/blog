
from app.models import Post,User,Comment
from app import db,photos
from flask_login import current_user
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

@main.route('/posts/add-post',methods = ['GET','POST'])
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
    current_user_id = current_user.id
    if current_user_id != 1:
        flash("You are not allowed to delete this post",category="error")
    else:
        if post:
            db.session.delete(post)
            db.session.commit()
            flash("Post deleted")         
        else:
            flash("Post could not be found", category="error")
            
    return redirect(url_for('main.index'))

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
    else:
        form.title.data = post.title
        form.body.data = post.text


    return render_template('admin/editpost.html',form = form)


@main.route('/user/profile/<int:id>')
def profile(id):
    id = 1
    user = User.query.filter_by(id = id).first()
    if user is None:
        flash("No such user",category="error")
        abort(404)
    
    return render_template('admin/profile.html',user = user,id = id)



@main.route('/user/<int:id>/edit/pic',methods = ['POST'])
def update_pic(id):

    user = User.query.filter_by(id = id).first()
    current_user_id = current_user.id

    if current_user_id != id:
        flash("You are not allowed to upload the profile picture",category="error")

    else:
        if 'photo' in request.files:
            photo = photos.save(request.files['photo'])
            filename= f'photos/{photo}'
            user.pic_path = filename
            db.session.commit()

    return redirect(url_for('main.profile',id = id))

@main.route('/user/<int:id>/edit',methods = ['POST','GET'])
def edit_profile(id):
    current_user_id = current_user
    user = User.query.filter_by(id = 1).first()
    id = 1
    
    if current_user_id != id:
        flash('You are not allowed to edit this page',category="error")
    
    else:
        if request.method == 'POST':
            pass
    

    return render_template('admin/editprofile.html',user = user,id = id)

@main.route('/add-comment/<int:id>',methods=['POST','GET'])
def add_comment(id):
    comment = request.form.get('comment')

    if not comment:
        flash("comment cannot be empty",category="error")
    else:
        post = Post.query.filter_by(id = id) 
        if post:
            comment = Comment(comment = comment , post_id = id,author = current_user.id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash('post not found',category="error")
    
    return redirect(url_for('main.index'))

@main.route('/comments/delete/<int:id>')
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    #   current_user.id == comment.author or current_user.id == one.author
    if comment:
        if current_user.id == comment.author or current_user.id == comment.post.author:
            db.session.delete(comment)
            db.session.commit()
        else:
            
            flash("You are not allowed to delete this comment")
    else:
        flash("Comment could not be found",category = "error")


    return redirect(url_for('main.index'))