from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length

class LoginForm(Form):
    usuario = StringField('Usuario', validators=[Required(), Length(1,64)])
    password = PasswordField('Contraseña', validators=[Required()])
    submit = SubmitField('Log In')