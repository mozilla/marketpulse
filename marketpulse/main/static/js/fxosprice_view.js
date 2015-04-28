$(document).ready(function() {
    'use strict';

    $('.delete-contribution').click(function () {
        $(this).find('.ask').hide();
        $(this).find('.delete-confirm').show();
    });

    $(document).on('click', '.cancel', function () {
        $(this).parents('.delete-contribution').find('.ask').show();
        $(this).closest('.delete-confirm').hide();
        return false;
    });
});
