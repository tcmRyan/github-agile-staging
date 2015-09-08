
from backend.models import Vendor
import os


def create_test(test):
    os.environ['TEST'] = test

if __name__ == '__main__':
    test = raw_input("Enter Test String: ")
    create_test(test)