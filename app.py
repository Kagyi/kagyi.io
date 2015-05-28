from flask import Flask, render_template, abort

import trainings
import functools
import sys

import sys
if sys.version_info > (3, 0):
    from flask_bootstrap import Bootstrap, WebCDN
else:
    from flask.ext.bootstrap import Bootstrap, WebCDN

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
        '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/'
    )
    return app

@functools.lru_cache(maxsize=None)
def get_courses():
    courses = [item for item in dir(trainings) if not item.startswith("__")]
    all_courses = []
    for course in courses:
        course_info = getattr(trainings, course)
        course_link = 'training/' + course
        course_info['course_link'] = course_link
        all_courses.append (course_info)
    return all_courses

app = create_app()

@app.route('/')
def homepage():
    return render_template('index.html', courses=get_courses())

@app.route('/training/<coursename>')
def trainingpage(coursename):
    try:
        course = getattr(trainings, coursename)
        return render_template('training.html',
                               courses=get_courses(),
                               training=course)
    except AttributeError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)