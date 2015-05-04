$(document).ready(function() {
    'use strict';
    var deleteContribution = $('.delete-contribution');

    $('#delete-ask').click(function () {
        deleteContribution.find('.ask').hide();
        deleteContribution.find('.delete-confirm').show();
    });

    $('.cancel').click(function () {
        deleteContribution.find('.ask').show();
        deleteContribution.find('.delete-confirm').hide();
    });
});
