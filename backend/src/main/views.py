from flask import Blueprint, render_template, session, redirect, url_for, jsonify, request
from flask_login import login_required, current_user

from ..forms import RegistrationForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        return redirect(url_for('index'))
    return render_template('register.html', form=form)
