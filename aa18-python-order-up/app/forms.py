from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
     employee_number=StringField("Employee number",validators=[DataRequired()])
     password=PasswordField("password",validators=[DataRequired()])
     submit=SubmitField("Login")
