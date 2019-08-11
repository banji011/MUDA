from flask import Flask 
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager 
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///muda.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)



today = datetime.utcnow()

class Works(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),unique=True, nullable=False)
    muda_role = db.Column(db.String(100),nullable=False)
    company = db.Column(db.String(100),nullable=False)
    short_desc = db.Column(db.String,nullable=False)
    desc = db.Column(db.String,nullable=False)
    work_image = db.Column(db.String(100),nullable=False, default='work_image.jpg')
    det_img1 = db.Column(db.String(100),nullable=True, default='det_image.jpg')
    det_img2 = db.Column(db.String(100),nullable=True, default='det_image.jpg')
    det_img3 = db.Column(db.String(100),nullable=True, default='det_image.jpg')
    work_video = db.Column(db.String(100), nullable=True)
    work_date = db.Column(db.String(50), default=today)

   
class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    message = db.Column(db.String(2000),nullable=False)
    contact_date = db.Column(db.String(50),default=today)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(50),nullable=False)
    post_content = db.Column(db.String(50), unique=True, nullable=False)
    post_image = db.Column(db.String(50), unique=True, default='blog.jpg')
    det_image = db.Column(db.String(50), unique=True, default='det_blog.jpg')
    post_date = db.Column(db.String(50), default=today)

    


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),unique=True, nullable=False)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(100),unique=True,nullable=False)
   
        


if __name__=='__main__':
    manager.run()