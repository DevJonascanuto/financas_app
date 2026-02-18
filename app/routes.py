from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import ReceitaForm, DespesaForm
from .models import Receita, Despesa, db

main = Blueprint("main", __name__)

@main.route("/")
@login_required
def dashboard():
    receitas = current_user.receitas
    despesas = current_user.despesas
    saldo = sum(r.valor for r in receitas) - sum(d.valor for d in despesas)
    return render_template("dashboard.html", receitas=receitas, despesas=despesas, saldo=saldo)

@main.route("/receita", methods=["GET", "POST"])
@login_required
def adicionar_receita():
    form = ReceitaForm()
    if form.validate_on_submit():
        nova = Receita(
            descricao=form.descricao.data,
            valor=form.valor.data,
            usuario=current_user
        )
        db.session.add(nova)
        db.session.commit()
        flash("Receita adicionada com sucesso!")
        return redirect(url_for("main.dashboard"))
    return render_template("form_receita.html", form=form)

@main.route("/despesa", methods=["GET", "POST"])
@login_required
def adicionar_despesa():
    form = DespesaForm()
    if form.validate_on_submit():
        nova = Despesa(
            descricao=form.descricao.data,
            valor=form.valor.data,
            usuario=current_user
        )
        db.session.add(nova)
        db.session.commit()
        flash("Despesa adicionada com sucesso!")
        return redirect(url_for("main.dashboard"))
    return render_template("form_despesa.html", form=form)
