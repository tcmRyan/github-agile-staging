from backend import app
from uuid import uuid4
from backend.models import Vendor
from binascii import unhexlify
from simplecrypt import decrypt
import urllib
from flask import abort, request
import requests
import urlparse

@app.route('/')
def index():
    url = make_authorization_url()
    text = '<a href="{url}">Authenticate with Github</a>'.format(url=url)
    return text

@app.route('/callback/github')
def github_callback():
    error = request.args.get('error')
    if error:
        return "Error: " + error
    state = request.args.get('state')
    if not is_valid_state(state):
        abort(403)
    code = request.args.get('code')
    results = get_token(code, state)
    token = results['access_token'][0]
    scope = results['scope'][0]
    return 'Token: {token}, Scope: {scope}'.format(token=token, scope=scope)

def make_authorization_url():
    # Generate a random string for teh state parameter
    # Save it for use later to prevent xsrf attacks
    state = str(uuid4())
    save_created_state(state)
    #TODO: Cache this
    vendor = Vendor.query.filter_by(name='github').first()
    client_id = decrypt_value(vendor.client_id)
    params = {
        "client_id": client_id,
        "state": state,
        "redirect_uri": "http://localhost:5000/callback/github",
        "scope": "user"
    }
    return "https://github.com/login/oauth/authorize?" + urllib.urlencode(params)


def get_token(code, state):
    vendor = Vendor.query.filter_by(name='github').first()
    client_id = decrypt_value(vendor.client_id)
    client_secret = decrypt_value(vendor.client_secret)
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'state': state,
    }
    response = requests.post('https://github.com/login/oauth/access_token', params=params)
    return urlparse.parse_qs(response.content)

def save_created_state(state):
    pass

def is_valid_state(state):
    return True

def decrypt_value(value):
    return decrypt(app.config['HASH_CHECK'], unhexlify(value))