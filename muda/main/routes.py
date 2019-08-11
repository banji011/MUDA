import os 
import secrets
from datetime import datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, Blueprint
from muda import db, bcrypt, mail
from muda.models import * 
from sqlalchemy import desc
from muda.main.forms import *
from flask_mail import Message


main = Blueprint('main', __name__)

@main.route('/')
def home():
    wk= Works.query.all()
    return render_template('homepage.html',wk=wk,title="This is Homepage content!")

@main.route('/project/<name>')
def project(name):
   wks = Works.query.filter_by(title=name).first()
   return render_template('works-details.html',wks=wks, title=wks.title)

@main.route('/about')
def about():
   return render_template('about.html', title="About Us Page")

@main.route('/contactus', methods=['GET','POST'])
def contact():
    form = ContactUsForm()
    if form.validate_on_submit():
        msg = Message('New Entry from MUDA', sender="MUDA CREATIVE ADMIN", recipients=[form.email.data])
        msg.body = f'''
        Name: {form.name.data}
        Email: {form.email.data}
        Message: {form.message.data}
         '''
        mail.send(msg)
        new_msg = ContactUs(name=form.name.data,email=form.email.data,message=form.message.data)
        db.session.add(new_msg)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('contact.html',form=form, title="Contact Us Page")


@main.route('/blog')
def blog():
   return render_template('blog.html', title="Blog Page")