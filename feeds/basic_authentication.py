import base64


def basic_authentication():
    USERNAME = "joshua"
    PASSWORD = "captureretail"
    en = base64.b64encode('%s:%s' % (USERNAME, PASSWORD))
    return en
