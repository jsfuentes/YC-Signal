import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    
    #Mongoengine Variables
    MONGODB_HOST='mongodb://admin:admin1@ds018238.mlab.com:18238/personal'
    MONGODB_DB='personal'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
