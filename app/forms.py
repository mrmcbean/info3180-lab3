from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Email,InputRequired

csrf_token = CSRFProtect()

def create_app():
    app = Flask(__name__)
    csrf.init_app(app)
    
    



class ContactForm(FlaskForm):


    name=StringField('Name', validators=[InputRequired("Enter your name")])
    email=StringField('Email', validators=[InputRequired("Enter your email address"),Email("Enter your email address")])
    subject=StringField('Subject', validators=[InputRequired("Enter a subject")])
    message=StringField('Message', validators=[InputRequired("Enter your message here")])

    submit=SubmitField("Send")

    

