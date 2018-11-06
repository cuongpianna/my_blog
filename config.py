class Config:
    CRSF_ENABLED = True
    SECRET_KEY = 'djkqu893u189dklasdklaj'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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
