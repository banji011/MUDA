from datetime import datetime
from flask import current_app
from muda import db, login_manager
from flask_login import UserMixin
from sqlalchemy import desc

today = datetime.today()

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

    def __repr__(self):
        return f"Works('{self.title}','{self.muda_role}','{self.company}','{self.short_desc}','{self.desc}','{self.work_date}')"

class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    message = db.Column(db.String(2000),nullable=False)
    contact_date = db.Column(db.String(50),default=today)

    def __repr__(self):
        return f"ContactUs('{self.name}','{self.email}','{self.message}','{self.contact_date}')"
        


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(50),nullable=False)
    post_content = db.Column(db.String(50), unique=True, nullable=False)
    post_image = db.Column(db.String(50), unique=True, default='blog.jpg')
    det_image = db.Column(db.String(50), unique=True, default='det_blog.jpg')
    post_date = db.Column(db.String(50), default=today)

    def __repr__(self):
        return f"Blog('{self.post_title}','{self.post_content}','{self.post_image}','{self.det_image}','{self.post_date}')"


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),unique=True, nullable=False)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(100),unique=True,nullable=False)

    def __repr__(self):
        return f"Admin('{self.email}','{self.username}')"
        