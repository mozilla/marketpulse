$(document).ready(function() {
    'use strict';

    var mapboxid = $('div#map').data('mapboxid');
    var mapboxtoken = $('div#map').data('mapboxtoken');
    var lat = $('div#map').data('lat');
    var lng = $('div#map').data('lng');

    L.mapbox.accessToken = mapboxtoken;
    L.mapbox.config.FORCE_HTTPS = true;
    var map = L.mapbox.map('map', mapboxid).setView([lat, lng], 16);
    L.marker([lat, lng], {
        icon: L.mapbox.marker.icon({
            'marker-symbol': 'star',
            'marker-color': '#ff8888'
        })
    }).addTo(map);
});
