from backend import db, app
from simplecrypt import encrypt
from binascii import hexlify


class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    client_id = db.Column(db.String(256))
    client_secret = db.Column(db.String(256))

    def __init__(self, name, client_id, client_secret):
        self.name = name
        self.client_id = hexlify(encrypt(app.config['HASH_CHECK'], client_id))
        self.client_secret = hexlify(encrypt(app.config['HASH_CHECK'], client_secret))

    def __repr__(self):
        return '<id {}>'.format(self.id)
