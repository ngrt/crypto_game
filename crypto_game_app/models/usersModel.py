from crypto_game_app.config import database

class User(database.db.Model):
    __tablename__ = 'users'
    id = database.db.Column(database.db.Integer, primary_key=True)
    public_id = database.db.Column(database.db.String(50), unique=True)
    name = database.db.Column(database.db.String(50))
    email = database.db.Column(database.db.String(50))
    password = database.db.Column(database.db.String(50))
    admin = database.db.Column(database.db.Boolean)
    wallet = database.db.relationship('Wallet', uselist=False, back_populates="users")
    transaction = database.db.relationship('Transaction', uselist=False, back_populates="users")

