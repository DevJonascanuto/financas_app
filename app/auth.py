from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .models import user, db
from .forms import LoginForm, RegisterForm

auth= Blueprint('"auth', __name__)


@auth.route("/login", methods=["GET, POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = user.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("main.dashboard"))
        
        flash("email ou senha invalidos")
    return render_template("login.html", form=form)

@auth.route("/register", methods=["GET", "POST"])
def register():
    form =RegisterForm()

    if form.validate_on_submit():
        user = user(email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("conta criada com sucesso")
        return redirect(url_for("auth.login"))
    
    return render_template("register.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
            
