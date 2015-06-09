from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap, WebCDN

import trainings, workshops

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
        '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/'
    )
    return app

def get_items_from_python_file(module):
    items = [item for item in dir(module) if not item.startswith("__")]
    all_items = []
    for item in items:
        item_info = getattr(module, item)
        item_link = '/learn/' + item.replace('_', '-')
        item_info['link'] = item_link
        all_items.append (item_info)
    return all_items

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

if __name__ == '__main__':
    app.run(debug=True)
