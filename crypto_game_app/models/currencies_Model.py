from crypto_game_app.config import database

class Currency(database.db.Model):
    __tablename__ = 'currencies'
    id = database.db.Column(database.db.Integer, primary_key=True)
    name = database.db.Column(database.db.String(50), unique=True)
    symbol = database.db.Column(database.db.String(1), unique=True)
    code = database.db.Column(database.db.String(3), unique=True)
