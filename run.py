import os
from flask import Flask, render_template, request, session, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'wid' #What Ive Done - Database
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost') #Ask tutoring at some point about what the second part means / is. 
mongo = PyMongo(app)
 
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
    record = {'user': user, 'achievement': achievement, 'time': time} 
    mongo.db.achievements.insert_one(record)
    
    #obj = {'foo':'bar'}
   # mongo.db.achievements.insert_one(obj)
    return render_template("today.html", title_of_page="Today - What I've Done", userID=session['userID']) 
    ## Explanation: render_template not redirect, because redirect caused issues with the username session variable.
    
@app.route('/today', methods=['GET', 'POST'])
def today():
    session['userID'] = request.form["username"] #stores username as userID
    return render_template("today.html", title_of_page="Today - What I've Done", userID=session['userID'])

@app.route('/history')
def history():
    return render_template("history.html", title_of_page="History - What I've Done", userID=session['userID'])
    
@app.route('/signout')
def signout():
    session.clear();
    return render_template("home.html", title_of_page="Home - What I've Done")

if __name__ == '__main__':
    app.secret_key = "SESSIONS_SECRET_KEY"     
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

