from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import Receita, Despesa, db
from .forms import ReceitaForm, DespesaForm

main = Blueprint("main", __name__)

@main.route("/")
@login_required
def dashboard():
    receitas = current_user.receitas
    despesas = current_user.despesas
    saldo = sum(r.valor for r in receitas) - sum(d.valor for d in despesas)
    return render_template("dashboard.html", receitas=receitas, despesas=despesas, saldo=saldo)

# Receitas
@main.route("/receita/adicionar", methods=["GET", "POST"])
@login_required
def adicionar_receita():
    form = ReceitaForm()
    if form.validate_on_submit():
        r = Receita(
            descricao=form.descricao.data,
            valor=form.valor.data,
            data=form.data.data,
            usuario=current_user
        )
        db.session.add(r)
        db.session.commit()
        flash("Receita adicionada!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("form_receita.html", form=form)

@main.route("/receita/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_receita(id):
    r = Receita.query.get_or_404(id)
    form = ReceitaForm(obj=r)
    if form.validate_on_submit():
        r.descricao = form.descricao.data
        r.valor = form.valor.data
        r.data = form.data.data
        db.session.commit()
        flash("Receita atualizada!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("form_receita.html", form=form)

@main.route("/receita/deletar/<int:id>")
@login_required
def deletar_receita(id):
    r = Receita.query.get_or_404(id)
    db.session.delete(r)
    db.session.commit()
    flash("Receita deletada!", "info")
    return redirect(url_for("main.dashboard"))

# Despesas
@main.route("/despesa/adicionar", methods=["GET", "POST"])
@login_required
def adicionar_despesa():
    form = DespesaForm()
    if form.validate_on_submit():
        d = Despesa(
            descricao=form.descricao.data,
            valor=form.valor.data,
            data=form.data.data,
            usuario=current_user
        )
        db.session.add(d)
        db.session.commit()
        flash("Despesa adicionada!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("form_despesa.html", form=form)

@main.route("/despesa/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_despesa(id):
    d = Despesa.query.get_or_404(id)
    form = DespesaForm(obj=d)
    if form.validate_on_submit():
        d.descricao = form.descricao.data
        d.valor = form.valor.data
        d.data = form.data.data
        db.session.commit()
        flash("Despesa atualizada!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("form_despesa.html", form=form)

@main.route("/despesa/deletar/<int:id>")
@login_required
def deletar_despesa(id):
    d = Despesa.query.get_or_404(id)
    db.session.delete(d)
    db.session.commit()
    flash("Despesa deletada!", "info")
    return redirect(url_for("main.dashboard"))
