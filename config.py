import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:@localhost/spaceship'
    # <DB TYPE>+<DB interface?>://<username>:<password>@<location>/<database>
    SQLALCHEMY_TRACK_MODIFICATIONS = False
