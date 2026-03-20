import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


df = pd.read_csv("dados/despesas_sujas.csv", on_bad_lines="skip")
print(f'linhas brutas: {len(df)}')

# ── 2. Padroniza nomes das colunas ───────────
df.columns = df.columns.str.strip().str.lower()
print("colunas: ", df.columns.tolist())

# ── 3. Remove espaços sobrando no texto ───────────

df["descricao"] = df["descricao"].str.strip()

# ── 4. Limpa e converte a coluna valor ────────────────────

df["valor"] = df["valor"].str.replace("R$", "", regex=False)
df["valor"] = df["valor"].str.strip()
df["valor"] = pd.to_numeric(df["valor"], errors= "coerce")

# ── 5. Converte datas (aceita DD/MM/AAAA e DD-MM-AAAA) ───

df["data"] = pd.to_datetime(df["data"], dayfirst=True, errors="coerce")
# ── 5. Converte datas ─────────────────────────────────────
df["data"] = pd.to_datetime(df["data"], dayfirst=True, errors="coerce")

# Remove linhas com data inválida
antes = len(df)
df = df.dropna(subset=["data"])
print(f"Linhas removidas por data inválida: {antes - len(df)}")

# ── 6. Remove linhas sem descrição ou sem valor ───────────
antes = len(df)
df = df.dropna(subset=["descricao", "valor"])
print(f"Linhas removidas por dados vazios: {antes - len(df)}")

# ── 7. Remove duplicatas (Enel e ENEL por exemplo) ────────
df["descricao"] = df["descricao"].str.capitalize()
antes = len(df)
df = df.drop_duplicates(subset=["descricao", "data"])
print(f"Duplicatas removidas: {antes - len(df)}")

# ── 8. Resultado final ────────────────────────────────────
print(f"\nLinhas prontas para inserir: {len(df)}")
print(df.to_string(index=False))

from financas_app.app import create_app, db
from financas_app.app.models import Despesa

app = create_app()

with app.app_context():
    for _, row in df.iterrows():
        despesa = Despesa(
            descricao  = row["descricao"],
            valor      = row["valor"],
            data       = row["data"],
            usuario_id = row["usuario_id"]
        )
        db.session.add(despesa)

    try:
        db.session.commit()
        print(f"{len(df)} despesas inseridas no banco!")
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao inserir: {e}")





