<<<<<<< HEAD
from app import create_app, db

app = create_app()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

=======
from financas_app.app import create_app

app = create_app()

if __name__ == "__main__":
>>>>>>> 7da8b58 (atualizando o app por completo, reestilizando, e incluindo funçoes de)
    app.run(debug=True)