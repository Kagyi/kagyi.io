from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, DecimalField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, Regexp, InputRequired, ValidationError

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

from utils import get_items_from_python_file
from trainers import keys
import trainings

allcourses = get_items_from_python_file(trainings)
course_choices = [(c['name'], c['title']) for c in allcourses]

class EnrollmentForm(Form):
    trainer_email = StringField('Trainer Email:', validators=[DataRequired(), Email()])
    trainer_keyfile = FileField('Trainer Keyfile:', validators=[DataRequired()])
    student_name = StringField('Student Name:', validators=[DataRequired()])
    student_email = StringField('Student Email:', validators=[DataRequired(), Email()])
    student_phone = StringField('Student Phone Number:', validators=[DataRequired()])
    student_address = TextAreaField('Student Address:', validators=[DataRequired()])

    course_name = SelectField('Course Name:', choices=course_choices, validators=[DataRequired()])
    course_fees = DecimalField('Course Fees:', validators=[DataRequired()])

    byod_student = BooleanField('<strong>BYOD Student</strong>')
    payment_received = BooleanField('<strong>I have received the course fees in full amount.</strong>')
    submit = SubmitField('Enroll')

    def validate_payment_received (form, field):
        if not field.data:
            raise ValidationError('Please, enroll only after you have received the course fees.')

    def validate_trainer_keyfile(form, field):
        trainer_email = form.trainer_email.data
        try:
            publickey = RSA.importKey(keys[trainer_email])
            privatekey = RSA.importKey(field.data.stream.read())

            hsh = SHA256.new(trainer_email).digest()
            signature = privatekey.sign(hsh, '')

            validkey = publickey.verify(hsh, signature)
            if not validkey: raise ValidationError('Invalid Keyfile.')

        except Exception:
            raise ValidationError('Invalid Keyfile.')
