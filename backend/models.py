from backend import db, flask_bcrypt, app


class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    client_id = db.Column(db.String(256))
    client_secret = db.Column(db.String(256))

    def __init__(self, name, client_id, client_secret):
        self.name = name
        self.client_id = flask_bcrypt.generate_password_hash(client_id, rounds=app.config['BCRYPT_LOG_ROUNDS'])
        self.client_secret = flask_bcrypt.generate_password_hash(client_secret, rounds=app.config['BCRYPT_LOG_ROUNDS'])

    def __repr__(self):
        return '<id {}>'.format(self.id)