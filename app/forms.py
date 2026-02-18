from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Cadastrar")

class ReceitaForm(FlaskForm):
    descricao = StringField("Descrição", validators=[DataRequired()])
    valor = FloatField("Valor", validators=[DataRequired()])
    submit = SubmitField("Adicionar Receita")

class DespesaForm(FlaskForm):
    descricao = StringField("Descrição", validators=[DataRequired()])
    valor = FloatField("Valor", validators=[DataRequired()])
    submit = SubmitField("Adicionar Despesa")

