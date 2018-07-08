from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user, login_user

from ..forms import RegistrationForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    print("Hit", request.method)
    flash("HI")

    if request.method == 'POST':
        if not form.validate():
            flash("Form validation fails")
            return render_template('register.html', form=form)
        user = User(form.email.data, form.password.data)
        print("HERE", user.email)
        user.save()
        login_user(user)
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)
