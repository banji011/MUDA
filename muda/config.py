import os 

class Config:
    SECRET_KEY = '39d64216c6a6732ef4b879075b5dc31f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///muda.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True 
    MAIL_USERNAME = 'mudacreativehub@gmail.com'
    MAIL_PASSWORD = 'thebamuda001'
