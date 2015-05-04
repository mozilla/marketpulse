$(document).ready(function() {
    'use strict';

    $(function() {
        $('.plan-form').formset({
            prefix: 'plans',
            deleteText: 'Remove price',
            addCssClass: 'btn btn-default',
            addText: 'Add another price',
            deleteCssClass: 'btn btn-default price-remove',
            added: addPrice,
            removed: removePrice
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

    function displayRemovePriceBtn() {
        var price_remove_btn = $('.price-remove');
        if ($('.planprices').length > 1) {
            price_remove_btn.show();
        } else {
            price_remove_btn.hide();
        }
    }

    function addPrice () {
        // Prepopulate currency with geocoding data
        var currency = $('.formset-currency:first').val();
        $('.formset-currency:not(:first)').val(currency);

        // Show price-remove button
        displayRemovePriceBtn();
    }

    function removePrice () {
        displayRemovePriceBtn();
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
    displayLocationForm();

    // Show checked formsets on load
    $('.hasplan-check:checked').closest('.switch').nextAll('.hasplan').slice(0, 4).show();

    // Show/Hide price formset remove button
    $('.price-remove').ready(displayRemovePriceBtn);
});
