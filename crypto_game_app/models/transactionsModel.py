from crypto_game_app.config import database

class Transaction(database.db.Model):
    __tablename__ = 'transactions'
    id = database.db.Column(database.db.Integer, primary_key=True)
    currency1 = database.db.Column(database.db.Integer)
    currency2 = database.db.Column(database.db.Integer)
    amount1 = database.db.Column(database.db.Float)
    amount2 = database.db.Column(database.db.Float)
    rate = database.db.Column(database.db.Float)
    user_id = database.db.Column(database.db.Integer, database.db.ForeignKey('users.id'))
    user = database.db.relationship("User", back_populates="transactions")