from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators= [DataRequired(),Email()])
    password = PasswordField("senha", validators=[DataRequired()]), Length(min=8)
    confirm = PasswordField("confirmar", validators=[EqualTo(password)])
    submit = SubmitField ("cadastrar")
