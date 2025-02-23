from flask import Flask, redirect, url_for, render_template
from datetime import datetime


app = Flask(__name__)

# Context processors
@app.context_processor
def date_now():
    return {
        'now': datetime.now()
    }

# Endpoints
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/say-hi/')
@app.route('/say-hi/<name>')
def sayHi(name="everyone"):
    if name.lower() == "world":
        return redirect(url_for('index'))
    else: 
        return render_template('sayHi.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)