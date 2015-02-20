import moneyed


FFXOS_ACTIVITY_NAME = 'Submit FirefoxOS device price'


def get_currency_choices():
    return sorted(((currency, data.code) for currency, data in moneyed.CURRENCIES.items()))
