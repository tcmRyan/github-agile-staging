from backend.models import Vendor
from backend import db


def create_vendor(vendor_name, client_id, client_secret):
    vendor = Vendor(vendor_name, client_id, client_secret)
    db.session.add(vendor)
    db.session.commit()

if __name__ == '__main__':
    vendor_name = raw_input("Enter Vendor Name: ")
    client_id = raw_input("Enter Client ID: ")
    client_secret = raw_input("Enter Client Secret: ")
    create_vendor(vendor_name, client_id, client_secret)