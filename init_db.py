from datetime import datetime
from app import create_app, db
from app.models import User, Receita, Despesa  # vamos assumir que você tenha esses modelos

app = create_app()

with app.app_context():
    # Cria todas as tabelas
    db.create_all()
    print("Tabelas criadas com sucesso!")

    # Verifica se já existe o usuário de teste
    if not User.query.filter_by(email="teste@teste.com").first():
        # Cria usuário de teste
        user = User(email="teste@teste.com")
        user.set_password("123456")
        db.session.add(user)
        db.session.commit()
        print("Usuário de teste criado: teste@teste.com / 123456")
    else:
        user = User.query.filter_by(email="teste@teste.com").first()
        print("Usuário de teste já existe.")

    # Adiciona algumas receitas de exemplo
    if not Receita.query.filter_by(usuario_id=user.id).first():
        receitas = [
            Receita(descricao="Salário", valor=5000.00, data=datetime(2026, 2, 1), usuario_id=user.id),
            Receita(descricao="Freelance", valor=1200.50, data=datetime(2026, 2, 10), usuario_id=user.id),
        ]
        db.session.add_all(receitas)
        print("Receitas de teste adicionadas.")

    # Adiciona algumas despesas de exemplo
    if not Despesa.query.filter_by(usuario_id=user.id).first():
        despesas = [
            Despesa(descricao="Aluguel", valor=1500.00, data=datetime(2026, 2, 5), usuario_id=user.id),
            Despesa(descricao="Supermercado", valor=450.75, data=datetime(2026, 2, 7), usuario_id=user.id),
        ]
        db.session.add_all(despesas)
        print("Despesas de teste adicionadas.")

    db.session.commit()
    print("Banco de dados inicializado com dados de teste!")
