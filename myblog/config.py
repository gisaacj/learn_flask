class Config(object):
    """Base config class."""
    SECRET_KEY = 'nobody will guess it'
    
class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/myblog'
