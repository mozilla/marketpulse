from urlparse import urljoin

from django.conf import settings

from django_countries import countries
import requests


COUNTRY_CODES = {key: value for (value, key) in list(countries)}


def reverse_geocode(lat, lng):
    """Query Mapbox API to get data for lat, lng"""

    query = '{0},{1}.json'.format(lng, lat)
    url = urljoin(settings.MAPBOX_GEOCODE_URL, query)
    params = {'access_token': settings.MAPBOX_TOKEN}
    response = requests.get(url, params=params)
    results = {}

    if response.status_code != 200:
        return results

    data = response.json()
    for feature in data['features']:
        text = feature['text']
        if feature['id'].startswith('country.'):
            try:
                results['country'] = COUNTRY_CODES[text]
            except KeyError:
                results['country'] = text
        if feature['id'].startswith('region.'):
            results['region'] = text
        if feature['id'].startswith('place.'):
            results['city'] = text
        if feature['id'].startswith('address.'):
            results['address'] = text
    return results
