from flask import Flask, render_template, abort, request, session, flash, redirect
from flask_bootstrap import Bootstrap, WebCDN

from forms import EnrollmentForm
from utils import get_items_from_python_file
import trainings, workshops

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
        '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/'
    )
    app.secret_key = 'lveyou'
    return app

app = create_app()
allcourses = get_items_from_python_file(trainings)
allworkshops = get_items_from_python_file(workshops)

@app.route('/')
def homepage():
    return render_template('index.html',
                           courses=allcourses,
                           workshops=allworkshops,
                       )

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
        form.course = getattr(trainings, form.course_name.data)
        invoice_html = render_template('invoice.html',
                                       submission=form)
        print invoice_html
        return invoice_html

    return render_template('enroll.html',
                           courses=allcourses,
                           workshops=allworkshops,
                           form=form)

if __name__ == '__main__':
    app.run(debug=True)
