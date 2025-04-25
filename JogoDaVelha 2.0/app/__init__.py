#Importação do flask e das funções da lógica do jogo.
from flask import Flask
from .routes import app_routes

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '@mara1290'
    app.register_blueprint(app_routes)

    return app
