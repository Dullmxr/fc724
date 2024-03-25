from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, RadioField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class DataCollectionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired()])
    grades = StringField('Grades', validators=[DataRequired()])
    suggestions_for_improvement = TextAreaField('Suggestions for Improvement', validators=[DataRequired()])
    satisfaction = RadioField('Satisfaction', choices=[('very satisfied', 'Very Satisfied'), ('satisfied', 'Satisfied'), ('balanced', 'Balanced'), ('dissatisfied', 'Unsatisfied')], validators=[DataRequired()])
    submit = SubmitField('Submit')