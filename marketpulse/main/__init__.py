import moneyed


FFXOS_ACTIVITY_NAME = 'Submit FirefoxOS device price'
FFXOS_MEDIA_ACTIVITY_NAME = 'Upload FirefoxOS media'


def get_currency_choices():
    return sorted(((currency, data.code) for currency, data in moneyed.CURRENCIES.items()))
