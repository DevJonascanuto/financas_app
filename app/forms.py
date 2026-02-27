from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirme a Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

class ReceitaForm(FlaskForm):
    descricao = StringField('Descrição', validators=[DataRequired(), Length(max=100)])
    valor = DecimalField('Valor', validators=[DataRequired(), NumberRange(min=0)])
    data = DateField('Data', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Salvar')

class DespesaForm(FlaskForm):
    descricao = StringField('Descrição', validators=[DataRequired(), Length(max=100)])
    valor = DecimalField('Valor', validators=[DataRequired(), NumberRange(min=0)])
    data = DateField('Data', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Salvar')
