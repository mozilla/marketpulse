$(document).ready(function() {
    'use strict';

    var mapboxid = $('div#map').data('mapboxid');
    var mapboxtoken = $('div#map').data('mapboxtoken');

    L.mapbox.accessToken = mapboxtoken;
    L.mapbox.config.FORCE_HTTPS = true;
    var map = L.mapbox.map('map', mapboxid).setView([29, 22.5], 2);
    var LocLayer = L.mapbox.featureLayer().addTo(map);
    map.locate();

    map.on('locationfound', function(e) {
        map.fitBounds(e.bounds);
        LocLayer.setGeoJSON({
            type: 'Feature',
            geometry: {
                type: 'Point',
                coordinates: [e.latlng.lng, e.latlng.lat]
            },
            properties: {
                'marker-color': '#ff8888',
                'marker-symbol': 'star'
            }
        });
        $('#location-text').html('Click on map for adjusting location.');
        $('#id_lat').val(e.latlng.lat);
        $('#id_lng').val(e.latlng.lng);

        var data = {
            'longitude': e.latlng.lng,
            'latitude': e.latlng.lat
        };

        $.ajax({
            url: '/fxosprice/new/',
            type: 'GET',
            dataType: 'json',
            data: data,
            success: function(json) {
                if ($('#error-div').length === 0) {
                    if (json.country !== null) {
                        $('#id_country').val(json.country);
                    }
                    if (json.currency !== null) {
                        $('.formset-currency').val(json.currency);
                    }
                }
            }
        });
    });

    map.on('click', function(e) {
        $('#location-text').html('Click on map for adjusting location.');
        LocLayer.setGeoJSON({
            type: 'Feature',
            geometry: {
                type: 'Point',
                coordinates: [e.latlng.lng, e.latlng.lat]
            },
            properties: {
                'marker-color': '#ff8888',
                'marker-symbol': 'star'
            }
        });
        $('#id_lat').val(e.latlng.lat);
        $('#id_lng').val(e.latlng.lng);
    });

    map.on('locationerror', function() {
        $('#location-text').html('Location error. Click on map for setting location');
    });
});
