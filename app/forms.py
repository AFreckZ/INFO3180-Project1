from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, DataRequired , Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    Title = StringField('Property_Title',validators =[InputRequired()])
    Description = TextAreaField('Description', validators=[InputRequired(' A text area for a message')])
    No_Room = IntegerField('No_Rooms', validators=[InputRequired()])
    No_Bathrooms = IntegerField('No_Bathrooms', validators=[InputRequired()])
    Price = IntegerField('Price', validators=[InputRequired()])
    Property_Type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    Location = StringField('Location',validators=[InputRequired()])
    Photo=FileField("Photo", validators=[FileRequired(),FileAllowed(["jpg", "png","jpeg","Images only!"])])
    