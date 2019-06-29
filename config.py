import os

class Config:
    
    SQLACHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_MODIFICATIONS = 'postgresql+psycopg2://nkimani:her1234@localhost/pitch'
    
    SECRET_KEY = "I'm not boarding"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")