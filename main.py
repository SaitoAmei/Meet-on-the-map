

from flask import Flask, abort, render_template, url_for, redirect, request, flash, session, make_response
import sqlite3
from geopy import *

from geo import *


def creation():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        us = """ CREATE TABLE IF NOT EXISTS users(name TEXT, pass TEXT, em TEXT, yo INT, male TEXT)"""
        cursor.execute(us)
        db.commit()


def inp_db(request):
            names=get_name()
            passwords=get_password()
            emails = get_email()
            serv_name_info = checkki(value=request.form['username'], base=names)
            serv_info_password = checkki(value=request.form['password'], base=passwords)
            serv_info_email = checkki(value=request.form['email'], base = emails)
            if serv_name_info == False and serv_info_password == False and serv_info_email==False:
                name = request.form['username']
                passw = request.form['password']
                email = request.form['email']
                age = request.form['age']
                male = request.form['sex']
                with sqlite3.connect('db/database.db') as db:
                    cursor = db.cursor()

                    cursor.execute("INSERT INTO users (name,pass,em,yo,male) VALUES(?,?,?,?,?)",(name,passw,email,age,male) )
            else: pass #flashmessage


def creat_event_base():
    with sqlite3.connect('db/events.db') as db:
        cursor=db.cursor()
        us=""" CREATE TABLE IF NOT EXISTS events(name TEXT, time  TEXT, date TEXT, description TEXT, participants INT, location TEXT, maker TEXT, limitation TEXT)"""
        cursor.execute(us)
        db.commit()


def get_email():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT em FROM users")
        title=cursor.fetchall()
    return title

def get_name():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT name FROM users")
        title=cursor.fetchall()
        print(title)
    return title

def dicty():
    names = get_name_event()
    locs = get_adres()
    descs = get_description()
    dates = get_date()
    times = get_time()
    makers = get_maker()
    limits = get_limitation()
    participants = get_participants()
    counter= len(names)
    events = []
    i=0
    while i<counter:
        events.append({"name": names[i], "description": descs[i],"location": locs[i], "date": dates[i], "time": times[i], "maker": makers[i], "limit": limits[i], "participant": participants[i]})
        i += 1
    print(events)
    return events
def add_event(request):
    creat_event_base()
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    description = request.form['description']
    participants = request.form['participants']
    location = request.form['location']
    maker = request.form['maker']
    limits = request.form['limitation']
    with sqlite3.connect('db/events.db') as db:
        cursor = db.cursor()

        cursor.execute("INSERT INTO events (name,time,date,description,participants,location,maker,limitation) VALUES(?,?,?,?,?,?,?,?)", (name,time, date,description,participants,location,maker,limits))
        db.commit()


def get_password():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT pass FROM users")
        title=cursor.fetchall()
    return title


def checkki(value,base):
    if any(value in tupl for tupl in base):
        return True
    else:
        return False

site=Flask(__name__)
site.config['SECRET_KEY'] = '23k42k3jf4f3f4kf234lo23f42ou34f23u4f32u4f2k3j4f23iu'



@site.route("/registration", methods=["POST","GET"])
def registry():
    coordin = geocoding(get_adres())
    if request.method == 'POST':
        creation()
        inp_db(request=request)
        flash('all fine', category='succes')
    return render_template('index_unreg.html', markers=coordin, events = dicty())

@site.route("/profile", methods=["POST","GET"])
def profile():
    coordin = geocoding(get_adres())
    username = request.cookies.get('user')
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(404)
    return render_template('index_reg.html', markers=coordin, events = dicty())
@site.errorhandler(404)
def user_permition(error):
    return render_template('eror.html')
@site.route("/login", methods=["POST","GET"])
def check():
        dictoos = dicty()
        if request.method == 'POST':
            coordin = geocoding(get_adres())
            names = get_name()
            passwords = get_password()
            serv_name_info = checkki(value=request.form['username'], base=names)
            serv_info_password = checkki(value=request.form['password'], base=passwords)
            resp = make_response()
            resp.set_cookie('user', request.form['username'], 60*60*24)

            if serv_name_info == True and serv_info_password == True:

                session['userLogged'] = request.form['username']
                resp.headers['location'] = url_for('profile')
                return resp, 302
                #return redirect(url_for('profile', username=session['userLogged']))


                #return render_template('index.html')
            elif serv_name_info == False and serv_info_password == False:
                return render_template('index_unreg.html', markers=coordin, events = dictoos)
            else:
                return render_template('50eror.html')

@site.route("/creation_events",methods=["POST","GET"])
def add_events():
    if request.method == 'POST':
        creat_event_base()
        add_event(request=request)
        return redirect("/map")
    #return render_template('index.html')

@site.route("/map")
def map():

    coordin = geocoding(get_adres())
    counter = len(get_name_event())
    if 'userLogged' in session:
        return render_template("index_reg.html", markers=coordin, events = dicty())

    else:
        return render_template("index_unreg.html", markers=coordin,  events = dicty())

@site.route('/')
def home():
   return redirect('/map')



if __name__ =='__main__':
   site.run(debug=True)





