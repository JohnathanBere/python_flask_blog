import os

SECRET_KEY = 'nargles'
DEBUG = True
DB_USERNAME = 'johnathanbere'
DB_PASSWORD = ''
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP', '127.0.0.1')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/home/ubuntu/workspace/flask_blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'