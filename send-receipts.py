import glob
import os
import cPickle
import requests
from weasyprint import HTML
from string import Template
from kagyi import app
from utils import get_submissions_path

def main():
    submissions = {}
    submissions_path = get_submissions_path(app.root_path)
    for submission_pkl in sorted(glob.glob(os.path.join(submissions_path, '*.pkl'))):
        with open(submission_pkl, 'rb') as submission_file:
            submission = cPickle.loads(submission_file.read())
            submissions[submission['student_email']] = submission
        os.unlink(submission_pkl)

    for s in submissions.values():
        weasy = HTML(string=s['receipt'])
        pdf_path = os.path.join(submissions_path, s['student_name'] + ".pdf")
        weasy.write_pdf(pdf_path)
        response = send_welcome_mail(s, pdf_path)
        print "Response " + str(response.status_code) + " for " + s['student_name']
        print response.json()
        os.unlink(pdf_path)

def send_welcome_mail(submission, pdf_path):
    subject = "Successfully Enrolled for the Course - " + submission['course']['title']
    to = submission['student_name'] + ' <' + submission['student_email'] + '>'

    template = Template("""
    Hey $student_name,

    This is just a confirmation email to inform you that we have received your enrollment for the course - $title. Please, see the attached pdf file for your enrollment details.

    See you at the top. Ugh, sorry, I meant at the class.
    """)

    variables = submission
    variables.update(submission['course'])
    text = template.substitute(variables)

    return requests.post(
        "https://api.mailgun.net/v3/sandbox178551b200274e9db1190b0f896ec9d6.mailgun.org/messages",
        auth=("api", app.config['MAIL_GUN_APIKEY']),
        files=[("attachment", open(pdf_path))],
        data={"from": "Thura Hlaing <thura@kagyi.io>",
              "to": to,
              "cc": submission['trainer_email'],
              "subject": subject,
              "text": text}
    )

if __name__ == "__main__":
    main()
