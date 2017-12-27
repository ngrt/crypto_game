from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from crypto_game_app import app


#SQLALCHEMY paramaters
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///config/crypto_game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from crypto_game_app.models import usersModel
from crypto_game_app.models import currencies_Model
from crypto_game_app.models import transactionsModel
from crypto_game_app.models import walletsModel