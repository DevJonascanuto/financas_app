
from financas_app.app import create_app, db
from financas_app.app.models import User, Receita, Despesa
from datetime import datetime

app = create_app()

with app.app_context():

    db.create_all()
    print("Banco criado!")

    if not User.query.filter_by(email="teste@teste.com").first():

        user = User(email="teste@teste.com")
        user.set_password("123456")
        db.session.add(user)
        db.session.commit()

        print("Usuário criado!")

