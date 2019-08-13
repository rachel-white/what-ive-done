import os
from flask import Flask, render_template, request

userID = ""

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'wid-dbr'
# - re-learn about what this line means, then edit as nessacery. app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        userID = request.username
    return render_template("home.html", title_of_page="userID")
        
@app.route('/about')
def about():
    return render_template("about.html", title_of_page="About - What I've Done")
    
@app.route('/aboutsi')
def aboutsi():
    return render_template("aboutsi.html", title_of_page="About - What I've Done")
    
@app.route('/today')
def today():
    return render_template("today.html", title_of_page="Today - What I've Done")

@app.route('/history')
def history():
    return render_template("history.html", title_of_page="History - What I've Done")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

