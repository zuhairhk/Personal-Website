from flask import Flask
from flask import render_template, send_file

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey123"

@app.route('/')
def index():
    return render_template('index.html')
    # return render_template('index.html')

@app.route('/paging')
def paging():
    return render_template('paging.html')

@app.route('/resume')
def resume():
    return send_file('resume.pdf')

@app.route('/epik_aim')
def aim():
    return send_file('epik_aim.mp4')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/tracks')
def tracks():
    return render_template('tracks.html')

@app.route('/rimi')
def rimi():
    return render_template('rimi.html')


if __name__ == '__main__':
    app.run(debug=True)