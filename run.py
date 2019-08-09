import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
        
@app.route('/about')
def about():
    return render_template("about.html")
    
@app.route('/aboutsi')
def aboutsi():
    return render_template("aboutsi.html")
    
@app.route('/today')
def today():
    return render_template("today.html")

@app.route('/history')
def history():
    return render_template("history.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
