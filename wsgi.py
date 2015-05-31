#!/usr/bin/env python
import os
from kagyi import app as application

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    #virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR','.'), '../python-env')
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.serve_forever()
