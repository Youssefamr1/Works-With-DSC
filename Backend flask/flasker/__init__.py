from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/') 
def index ():
    return render_template('index.html')

@app.route('/search') 
def serach ():
    return render_template('results.html')    