import pandas as pd
import sys
import os

# ── Aponta para a raiz do projeto ────────────────────────
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from financas_app.app import create_app, db
from financas_app.app.models import Despesa, Receita

app = create_app()

# ── Lê os CSVs ───────────────────────────────────────────
df_despesas = pd.read_csv("dados/despesas.csv")
df_receitas = pd.read_csv("dados/receitas.csv")

print(f"Despesas encontradas: {len(df_despesas)}")
print(f"Receitas encontradas: {len(df_receitas)}")

# ── Insere no banco ───────────────────────────────────────
with app.app_context():
    for _, row in df_despesas.iterrows():
        despesa = Despesa(
            descricao  = row["descricao"],
            valor      = row["valor"],
            data       = pd.to_datetime(row["data"]),
            usuario_id = row["usuario_id"]
        )
        db.session.add(despesa)

    for _, row in df_receitas.iterrows():
        receita = Receita(
            descricao  = row["descricao"],
            valor      = row["valor"],
            data       = pd.to_datetime(row["data"]),
            usuario_id = row["usuario_id"]
        )
        db.session.add(receita)

    try:
        db.session.commit()
        print(f"{len(df_despesas)} despesas inseridas!")
        print(f"{len(df_receitas)} receitas inseridas!")
        print("Concluído!")
    except Exception as e:
        db.session.rollback()
        print(f"Erro: {e}")