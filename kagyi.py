from flask import Flask, render_template, abort, request, session, flash, redirect
from flask_bootstrap import Bootstrap, WebCDN

from forms import EnrollmentForm
from utils import get_items_from_python_file
import trainings, workshops
import cPickle, time, os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config')
    Bootstrap(app)
    app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
        '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/'
    )
    app.secret_key = app.config['SECRET_KEY']
    return app

app = create_app()
allcourses = get_items_from_python_file(trainings)
allworkshops = get_items_from_python_file(workshops)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def homepage():
    return render_template('index.html',
                           courses=allcourses,
                           workshops=allworkshops)

@app.route('/learn/<coursename>')
def learningpage(coursename):
    coursename = coursename.replace('-', '_')
    if coursename in workshops.__dict__:
        course = getattr(workshops, coursename)
    elif coursename in trainings.__dict__:
        course = getattr(trainings, coursename)
    else:
        abort(404)

    return render_template('training.html',
                           courses=allcourses,
                           workshops=allworkshops,
                           training=course)

@app.route('/googleebd0e4b919c0e268.html')
def domain_verification():
    return app.send_static_file('googleebd0e4b919c0e268.html')

@app.route('/enroll', methods=['POST', 'GET'])
def enroll():
    form = EnrollmentForm()
    if form.validate_on_submit():
        submission = form.data
        course = getattr(trainings, submission['course_name'])
        submission['course'] = {
            'name' : course['name'],
            'title': course['title']
        }

        receipt = render_template('invoice.html', submission=submission)
        submission['receipt'] = receipt
        del submission['trainer_keyfile']
        timestamp = int(time.time())

        submission_path = os.path.join (ROOT_PATH, 'submissions', str(timestamp) + '.pkl')
        with open(submission_path , 'wb') as pickleFile:
            cPickle.dump (submission, pickleFile, -1)
        return receipt

    return render_template('enroll.html',
                           courses=allcourses,
                           workshops=allworkshops,
                           form=form)

if __name__ == '__main__':
    app.run()
