$(document).ready(function() {
    'use strict';

    $(function() {
        $('.planprices').formset({
            prefix: 'plans',
            deleteText: 'Remove price',
            addCssClass: 'btn btn-default',
            addText: 'Add another price',
            deleteCssClass: 'btn btn-default',
            added: changeCurrency,
      });
    });

    function displayLocationForm () {
        var choice = $('#id_is_online:checked').val();

        if (choice === 'on') {
            $('#location').hide();
            $('#onlineshop').show();
        } else {
            $('#location').show();
            $('#onlineshop').hide();
        }
    }

    function changeCurrency () {
        var currency = $('.formset-currency:first').val();
        $('.formset-currency:not(:first)').val(currency);
    }

    $(document).on('click', '.hasplan-check', function () {
        var choice = $(this).closest('.switch').nextAll('.hasplan').slice(0, 4);

        if (this.checked) {
            choice.show();
        } else {
            choice.hide();
        }
    });

    // Show location form if contribution is online
    $('#id_is_online').on('change', displayLocationForm);

    // Show checked formsets on load
    $('.hasplan-check:checked').closest('.switch').nextAll('.hasplan').slice(0, 4).show();

    displayLocationForm();
});
