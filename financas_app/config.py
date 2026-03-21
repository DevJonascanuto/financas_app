import os

class config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")

    DATABASE_URL = os.getenv("DATABASE_URL", 
        "mysql+pymysql://financas:123456@localhost/financas_db")
    
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False