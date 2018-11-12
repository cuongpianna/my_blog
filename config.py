import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'app\\uploads')

class Config:
    CRSF_ENABLED = True
    SECRET_KEY = 'djkqu893u189dklasdklaj'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = UPLOAD_FOLDER


class DevelopementConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/myblog'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/myblog'


config = {
    'development': DevelopementConfig,
    'default': DevelopementConfig,
    'production': ProductionConfig
}
