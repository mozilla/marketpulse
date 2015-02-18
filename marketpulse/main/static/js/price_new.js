$(document).ready(function() {
    "use strict";

    $("#planprices-addfield").click(function() {
        $(".planprices:first").clone().appendTo("#fieldset-planprices");
        return false;
    });

    $("#onlineshop-check").click(function() {
        var n = $("#onlineshop-check:checked").length;
        if (n === 0) {
            $("#location").show();
            $("#onlineshop").hide();
        } else {
            $("#location").hide();
            $("#onlineshop").show();
        }
    });

    $(document).on("click", ".hasplan-check", function () {
        var n = $(this.checked).length;

        if (n === 0) {
            console.log(n);
            $(this).closest(".planprices").find(".hasplan").hide();
        } else {
            console.log(n);
            $(this).closest(".planprices").find(".hasplan").show();
        }
    });
});
