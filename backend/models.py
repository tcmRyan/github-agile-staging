from backend import db, flask_bcrypt, app
from sqlalchemy.ext.hybrid import hybrid_property


class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    _client_id = db.Column(db.Strign(256))
    _client_secret = db.Column(db.String(256))

    @hybrid_property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def _set_client_id(self, plaintext):
        self._client_id = flask_bcrypt.generate_password_hash(plaintext, rounds=app.config['BCRYPT_LOG_ROUNDS'])

    @hybrid_property
    def client_secret(self):
        return self._client_secret

    @client_secret.setter
    def _set_client_secret(self, plaintext):
        self._client_secret = flask_bcrypt.generate_password_hash(plaintext, rounds=app.config['BCRYPT_LOG_ROUNDS'])