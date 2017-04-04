from os import path
from uuid import uuid4
from flask import flash,url_for,redirect,render_template,Blueprint
from myblog.forms import LoginForm,RegisterForm
from myblog.models import db,User

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder = path.join(path.pardir,'template','main'))

@main_blueprint.route('/')
def index():
    return redirect(url_for('blog.home'))

@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """View function for login."""

    # Will be check the account whether rigjt.
    form = LoginForm()
    openid_form = OpenIDForm()
    
    if openid_form.validate_on_submit():
        return openid.trg_login(
            openid_form.openid_url.data,
            ask_for=['nickname', 'email'],
            ask_for_optional=['fullname'])
    
    openid_errors = openid.fetch_error()
    if openid_errors:
        flash(openid_errors, category="danger")


    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()

        # Using the Flask-Login to processing and check the login status for user
        # Remember the user's login status. 
        login_user(user, remember=form.remember.data)

        identity_changed.send(
            current_app._get_current_object(),
            identity=Identity(user.id))

        flash("You have been logged in.", category="success")
        return redirect(url_for('blog.home'))

    return render_template('login.html',
                           form=form,
                           openid_form=openid_form)

@main_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    """View function for logout."""

    logout_user()

    identity_changed.send(
        current_app._get_current_object(),
        identity=AnonymousIdentity())
    flash("You have been logged out.", category="success")
    return redirect(url_for('main.login'))

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """View function for Register."""

    # Will be check the username whether exist.
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(id=str(uuid4()),
                        username=form.username.data,
                        password=form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Your user has been created, please login.',
              category="success")

        return redirect(url_for('main.login'))
    return render_template('register.html',
                           form=form)
