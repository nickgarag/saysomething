import os

class Config(object):
    SECRET_KEY = os.environ.get('SSN_SECRET_KEY') or 'xxxx'
    SUBJECT_NAME = os.environ.get('SSN_SUBJECT_NAME') or 'someone'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SSN_SQLALCHEMY_DATABASE_URI') or 'sqlite:///./sql.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CAPTCHA_CONFIG = {}
    CAPTCHA_CONFIG['SECRET_CSRF_KEY'] = os.environ.get('SSN_CAPTCHA_SECRET_CSRF_KEY') or "secretssssssssssssssssskey"
    CAPTCHA_CONFIG['CAPTCHA_LENGTH'] = 12
