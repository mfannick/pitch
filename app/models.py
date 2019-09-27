from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index =True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(5000))
    profile_pic_path = db.Column(db.String)
    pass_secure = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    pitchId = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    commentId = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitchTitle = db.Column(db.String)
    pitchWrite = db.Column(db.String(1000))
    category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    userId = db.Column(db.Integer,db.ForeignKey("users.id"))
    # upVotes = db.Column(db.Integer)
    # downVotes = db.Column(db.Integer)
    commentId = db.relationship('Comment',backref =  'pitch',lazy = "dynamic")

    def savePitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def getPitches(cls,category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches

    @classmethod
    def getPitch(cls,id):
        pitch = Pitch.query.filter_by(id=id).first()

        return pitch

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    commentWrite = db.Column(db.String(1000))
    timeComment = db.Column(db.DateTime,default=datetime.utcnow)
    userId= db.Column(db.Integer,db.ForeignKey("users.id"))
    pitchId = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def saveComment(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def getComment(cls,commentWrite):
        commentWrite = Comment.query.filter_by(commentWrite=commentWrite).all()
        # comment = Comment.query.order_by(
        #    Comment.timeComment.desc()).filter_by(id=id).all()
        return commentWrite

