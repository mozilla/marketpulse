$(document).ready(function() {
    $('#planprices-addfield').click(function() {
        $("#planprices").clone().appendTo("#fieldset-planprices");
        return false;
    });

    $('#onlineshop-check').click(function() {
        var n = $("#onlineshop-check:checked").length;
        if (n == 0) {
            $("#location").show();
            $("#onlineshop").hide();
        } else {
            $("#location").hide();
            $("#onlineshop").show();
        }
    });
});