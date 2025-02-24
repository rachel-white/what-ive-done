import os
from flask import Flask, render_template, request, session, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'wid' #What Ive Done - Database
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
mongo = PyMongo(app)

now = datetime.now() # current date and time
day_name = now.strftime("%a")
month_name = now.strftime("%b") 
day_in_month = now.strftime("%d")
year = now.strftime("%Y")
today_date = day_name + " " + month_name + " " + day_in_month + " " + year
print(today_date)
#date "Mon Aug 26 2019"
#today_date: Tue Sep:17:2019

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", title_of_page="Home - What I've Done")
    
@app.route('/about')
def about():
    return render_template("about.html", title_of_page="About - What I've Done")
    
@app.route('/aboutsi')
def aboutsi():
    return render_template("aboutsi.html", title_of_page="About - What I've Done")
    
@app.route('/add_achievement', methods=['GET', 'POST'])
def add_achievement():
    achievement = request.form["achievement"]
    user = session['userID']
    time = request.form["time"]
    date =request.form["date"]
    record = {'user': user, 'achievement': achievement, 'time': time, 'date': date} 
    mongo.db.achievements.insert_one(record)
    return render_template("today.html", title_of_page="Today - What I've Done", userID=session['userID'], achievements=mongo.db.achievements.find({"user": session['userID'], "date": today_date})) 
    ## Explanation: render_template not redirect, because redirect caused issues with the username session variable.
    
@app.route('/today', methods=['GET', 'POST'])
def today():
    session['userID'] = request.form["username"] #stores username as userID
    #return render_template("today.html", title_of_page="Today - What I've Done", userID=session['userID'], achievements=mongo.db.achievements.find({"user": session['userID'], "date": today_date}))
    return render_template("today.html", title_of_page="Today - What I've Done", userID=session['userID'], achievements=mongo.db.achievements.find({"user": session['userID'], "date": today_date}))

@app.route('/history')
def history():
    return render_template("history.html", title_of_page="History - What I've Done", userID=session['userID'], history=mongo.db.achievements.find({"user": session['userID']}))
    
    
@app.route('/signout')
def signout():
    session.clear();
    return render_template("home.html", title_of_page="Home - What I've Done")

if __name__ == '__main__':
    app.secret_key = "SESSIONS_SECRET_KEY"     
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

