from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length

class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1,64)])
    password = PasswordField('Contraseña', validators=[Required()])
    submit = SubmitField('Log In')