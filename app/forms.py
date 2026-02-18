from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField("Confirme a senha", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Cadastrar")

class ReceitaForm(FlaskForm):
    descricao = StringField("Descrição", validators=[DataRequired()])
    valor = FloatField("Valor", validators=[DataRequired()])
    data = DateField("Data", validators=[DataRequired()])
    submit = SubmitField("Salvar")

class DespesaForm(FlaskForm):
    descricao = StringField("Descrição", validators=[DataRequired()])
    valor = FloatField("Valor", validators=[DataRequired()])
    data = DateField("Data", validators=[DataRequired()])
    submit = SubmitField("Salvar")
