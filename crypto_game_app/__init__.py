from flask import Flask
from crypto_game_app.main.controllers import main
from crypto_game_app.admin.controllers import admin

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')