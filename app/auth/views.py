from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from .. models import Usuario
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST']) 
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(nombre_usuario=form.usuario.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, False)
            return redirect(request.args.get('next') or url_for('main.home'))
        flash('Usuario o contraseña incorrectos')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has hecho logout')
    return redirect(url_for('.login'))