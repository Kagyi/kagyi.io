from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap, WebCDN

import trainings
import functools

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
        '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/'
    )
    return app


def get_courses():
    courses = [item for item in dir(trainings) if not item.startswith("__")]
    all_courses = []
    for course in courses:
        course_info = getattr(trainings, course)
        course_link = '/learn/' + course
        course_info['course_link'] = course_link
        all_courses.append (course_info)
    return all_courses

app = create_app()
allcourses = get_courses()

@app.route('/')
def homepage():
    return render_template('index.html', courses=allcourses)

@app.route('/learn/<coursename>')
def trainingpage(coursename):
    try:
        course = getattr(trainings, coursename)
        return render_template('training.html',
                               courses=allcourses,
                               training=course)
    except AttributeError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
