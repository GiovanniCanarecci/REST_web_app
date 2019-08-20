# forms.py
from flask_wtf.html5 import URLField
from wtforms import Form, StringField, SelectField, validators

class First_Action_Form(Form):
    choices = [('Write a New Message', 'Write a New Message'),
               ("See Saved Messages", "See Saved Messages")]
    selection = SelectField('Please choose:', choices=choices)
    search=StringField('')

class Basic_Form(Form):
    choices = [("Show advance data and options", "Show advance data and options"),
               ("Back to mainpage", "Back to mainpage")]
    selection = SelectField('Please choose:', choices=choices)
    search=StringField('')

class Advanced_Form(Form):
    choices = [("Show basic data", "Show basic data"),
               ("Back to mainpage", "Back to mainpage"),
               ("Download as JSON", "Download as JSON"),
               ("Download as XML", "Download as XML"),]
    selection = SelectField('Please choose:', choices=choices)
    search=StringField('')

class Messages_Form(Form):
    title = StringField('Title', 
            [validators.DataRequired(message="Enter the title here")], 
            render_kw={'maxlength': 100})
    content = StringField('Content', 
            [validators.DataRequired(message="Enter Your message here")], 
            render_kw={'maxlength': 1000})
    sender = StringField('Sender', 
            [validators.DataRequired(message="Enter Your name here")], 
            render_kw={'maxlength': 100})
    url = URLField('URL (add http://)', 
            [validators.DataRequired(message="Enter URL Please"), 
            validators.URL(message="Enter Valid URL Please.")])