from flask import Flask, redirect, url_for

<<<<<<< HEAD
from myblog.models import db
from myblog.controllers import blog,main
from myblog.extensions import bcrypt
=======
from models import db
from controllers import blog
>>>>>>> d9e898ed46d581d82db757af11c1a970699e5b49

def create_app(object_name):
    """Create the app instance via `Factory Method`"""

    app = Flask(__name__)
    # Set the app config 
    app.config.from_object(object_name)

    # Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
    db.init_app(app)
<<<<<<< HEAD
    bcrypt.init_app(app)
=======
>>>>>>> d9e898ed46d581d82db757af11c1a970699e5b49

    @app.route('/')
    def index():
        # Redirect the Request_url '/' to '/blog/'
        return redirect(url_for('blog.home'))

    # Register the Blueprint into app object
    app.register_blueprint(blog.blog_blueprint)
<<<<<<< HEAD
    app.register_blueprint(main.main_blueprint)
=======
>>>>>>> d9e898ed46d581d82db757af11c1a970699e5b49

    return app
