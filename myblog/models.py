# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from myblog.extensions import bcrypt 

# INIT the sqlalchemy object
# Will be load the SQLALCHEMY_DATABASE_URI from config.py
# SQLAlchemy 会自动的从app对象中的 Devconfig 中加载连接数据库的配置项
db = SQLAlchemy()

posts_tags = db.Table('posts_tags',
    db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
    db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))

users_roles = db.Table('users_roles',
    db.Column('user_id', db.String(45), db.ForeignKey('users.id')),
    db.Column('role_id', db.String(45), db.ForeignKey('roles.id')))

class User(db.Model):
    """Represents Proected users."""

    __tablename__='users'
    id = db.Column(db.String(45),primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # Establish contact with Post's ForeignKey: user_id
    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic')


    roles = db.relationship(
        'Role',
        secondary=users_roles,
        backref=db.backref('users', lazy='dynamic'))

    def __init__(self,id,username,password):
        self.id = id;
        self.username = username
        self.password = self.set_password(password)

        default = Role.query.filter_by(name="default").one()
        self.roles.append(default)

    def __init__(self,id,username,password):
        self.id = id;
        self.username = username
        self.password = password

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)

    def set_password(self, password):
        """Convert the password to cryptograph via flask-bcrypt"""
        return bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def is_authenticated(self):
        """Check the user whether logged in."""

        # Check the User's instance whether Class AnonymousUserMixin's instance.
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active():
        """Check the user whether pass the activation process."""

        return True

    def is_anonymous(self):
        """Check the user's login status whether is anonymous."""

        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        """Get the user's uuid from database."""

        return unicode(self.id)

class Role(db.Model):
    """Represents Proected roles."""
    __tablename__ = 'roles'

    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Role `{}`>".format(self.name)

class Post(db.Model):
    """Represent Proected posts."""

    __tablename__='posts'
    id = db.Column(db.String(45),primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # Set the foreign key for Post
    user_id = db.Column(db.String(45),db.ForeignKey('users.id'))
    # Establish contact with Comment's ForeignKey:post_id
    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic')
    # many to many:posts<==>tags
    tags = db.relationship(
        'Tag',
        secondary=posts_tags,
        backref=db.backref('posts',lazy='dynamic'))

    def __init__(self,title):
        self.title = title

    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)

class Tag(db.Model):
    """Represents Proected tags."""

    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Model Tag `{}`>".format(self.name)

class Comment(db.Model):
    """Represents Proected comments."""

    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Model Comment `{}`>'.format(self.name)
