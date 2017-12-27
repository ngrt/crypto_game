from crypto_game_app.config import database

class Wallet(database.db.Model):
    __tablename__ = 'wallets'
    id = database.db.Column(database.db.Integer, primary_key=True)
    dollar = database.db.Column(database.db.Float)
    bitcoin = database.db.Column(database.db.Float)
    user_id = database.db.Column(database.db.Integer, database.db.ForeignKey('users.id'))
    user = database.db.relationship("User", back_populates="wallets")