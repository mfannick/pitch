from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,RadioField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    

class PitchForm(FlaskForm):
    pitchTitle= StringField('Your pitch title',validators=[Required()])
    pitchWrite=  TextAreaField('Write your pitch',validators =[Required()])
    category = RadioField('Label', choices=[('interview', 'interview'), ('product', 'product'),('promotion', 'promotion')])
    submitPitch= SubmitField('Submit')
class CommentForm(FlaskForm):
	commentWrite = TextAreaField('Add comment',validators=[Required()])
	submitComment = SubmitField('Submit')

