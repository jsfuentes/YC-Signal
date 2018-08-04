from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user, login_user

from ..models import User
from ..forms import RegistrationForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = RegistrationForm(request.form)
        print(request.headers['Content-Type'])
        print(request.data)
        print("Hit", request.form)
        if not form.validate():
            flash("Form validation fails")
            return render_template('register.html', form=form)
        user = User(form.email.data, form.password.data)
        user.save()
        login_user(user)
        flash('Im a flash: Thanks for registering')
        return redirect(url_for('main.index'))

    return render_template('register.html')
