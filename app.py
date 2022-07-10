from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('paging.html')
    # CHANGE WHEN COMPLETE --> return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/tracks')
def tracks():
    return render_template('tracks.html')

if __name__ == '__main__':
    app.run(debug=True)