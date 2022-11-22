import datetime

USER = 'user'
PASSWORD = 'bitnami'
PRODUCT_NAME = 'PRODUCT_NAME'
PRODUCT_TAG = 'PRODUCT_TAG'
PRODUCT_MODEL = 'PRODUCT_MODEL'

NEW_USER_FIRSTNAME = 'NEW_USER_FIRSTNAME'
NEW_USER_LASTNAME = 'NEW_USER_LASTNAME'
NEW_USER_TELEPHONE = '1234'
NEW_USER_PASSWORD = 'NEW_USER_PASSWORD'

currencies = {'$', '€', '£'}


def generate_product_name():
    return PRODUCT_NAME + str(datetime.datetime.now())


def generate_product_tag():
    return PRODUCT_TAG + str(datetime.datetime.now())


def generate_product_model():
    return PRODUCT_MODEL + str(datetime.datetime.now())


def generate_uniq_email():
    return str(hash(str(datetime.datetime.now()))) + '@email.enmil'