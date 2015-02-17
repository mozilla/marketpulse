$(document).ready(function() {
    'use strict';

    var mapboxid = $('div#map').data('mapboxid');
    var mapboxtoken = $('div#map').data('mapboxtoken');

    L.mapbox.accessToken = mapboxtoken;
    L.mapbox.config.FORCE_HTTPS = true;
    var map = L.mapbox.map("map", mapboxid).setView([29, 22.5], 2);;
    var LocLayer = L.mapbox.featureLayer().addTo(map);
    map.locate();

    map.on("locationfound", function(e) {
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
        $('#location-text').html("Click on map for adjusting location.");
        $("#lat").val(e.latlng.lat);
        $("#lon").val(e.latlng.lng);
    });

    map.on('click', function(e) {
        $("#location-text").html("Click on map for adjusting location.");
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
        $("#lat").val(e.latlng.lat);
        $("#lon").val(e.latlng.lng);
    });

    map.on('locationerror', function() {
        $('#location-text').html("Location error. Click on map for setting location");
    });
});
