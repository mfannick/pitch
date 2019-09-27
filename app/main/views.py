from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .. import db,photos
from .forms import UpdateProfile,PitchForm,CommentForm
from flask_login import login_required,current_user
import datetime

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Pitching website'
    pitchInterview = Pitch.query.filter_by(category='interview')
    pitchProduct = Pitch.query.filter_by(category='product')
    pitchPromotion = Pitch.query.filter_by(category='promotion')
    return render_template('index.html',title = title, interview = pitchInterview, product = pitchProduct, promotion = pitchPromotion)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form = form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def pitchNew():
    form = PitchForm()
    if form.validate_on_submit():
        pitchTitle = form.pitchTitle.data
        pitchWrite = form.pitchWrite.data
        pitchCategory = form.category.data
        new_pitch = Pitch(pitchTitle=pitchTitle,pitchWrite=pitchWrite,category=pitchCategory,user=current_user)
        new_pitch.savePitch()
        return redirect(url_for('.index'))
    title = 'New pitch'
    return render_template('pitch.html',title = title,pitch_form=form )



@main.route('/pitches/pitchInterview')
def pitchInterview():
    pitches = Pitch.getPitches('interview')
    return render_template("pitchInterview.html", pitches = pitches)


@main.route('/pitches/pitchProduct')
def pitchProduct():
    pitches = Pitch.getPitches('product')
    return render_template("pitchProduct.html", pitches = pitches)


@main.route('/pitches/pitchPromotion')
def pitchPromotion():
    pitches = Pitch.getPitches('promotion')
    return render_template("pitchPromotion.html", pitches = pitches)

    

@main.route('/comment/new/<int:pitchId>', methods = ['GET','POST'])
@login_required
def commentPitch(pitchId):
   form = CommentForm()
   pitch=Pitch.query.get(pitchId)
   if form.validate_on_submit():
       commentWrite = form.commentWrite.data
       new_comment = Comment(commentWrite = commentWrite, userId = current_user._get_current_object().id, pitchId = pitch.id)
       db.session.add(new_comment)
       db.session.commit()
       return redirect(url_for('.commentPitch', pitchId= pitch.id))
   comments = Comment.query.filter_by(pitchId = pitch.id).all()
   return render_template('comment.html', comment_form = form, comments = comments, pitch = pitch )


