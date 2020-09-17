from flask import render_template, redirect, request, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. models import Usuario
from .forms import LoginForm
from .. import oauth
import os

#oauth config
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
google = oauth.register(
    name='google',
    client_id=os.environ['GOOGLE_LOGIN_CLIENT_ID'],
    client_secret=os.environ['GOOGLE_LOGIN_CLIENT_SECRET'],
    # access_token_url='https://accounts.google.com/o/oauth2/token',
    # access_token_params=None,
    # authorize_url='https://accounts.google.com/o/oauth2/auth',
    # authorize_params=None,
    server_metadata_url=CONF_URL,
    api_base_url='https://www.googleapis.com/oauth2/v1',
    client_kwargs={'scope': 'openid profile email'}
)

@auth.route('/login', methods=['GET', 'POST']) 
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, False)
            session['email'] = form.email.data
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Usuario o contraseña incorrectos')
    return render_template('auth/login.html', form=form)

@auth.route('/google')
def login_google():
    redirect_uri = url_for('auth.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@auth.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    user = google.parse_id_token(token)
    authuser = Usuario.query.filter_by(email=user.email).first()
    if authuser is not None:
        login_user(authuser, False)
        session['email'] = user.email
        return redirect(request.args.get('next') or url_for('main.index'))
    print(user)
    return redirect('/')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has hecho logout')
    return redirect(url_for('.login'))
