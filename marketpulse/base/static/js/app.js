jQuery(document).ready(function ($) {
    "use strict";

    Tabzilla.disableEasterEgg();


    /* Navigation Menu */

    // Collapse Nav menu when user clicks outside the dropdown
    function collapseNavMenu() {
        $("#dropdown-menu").hide();
        $("#dropdown-menu").removeClass("open");
        $("#outer-wrapper").off("click", collapseNavMenu);
    }

    // Expand Nav menu
    function expandNavMenu(e) {
        var $menu = $("#dropdown-menu");
        e.stopPropagation();

        $menu.toggle();
        $menu.toggleClass("open");

        // If the nav is open listen for clicks outside the dropdown
        if ($menu.hasClass("open")) {
            $("#outer-wrapper").on("click", collapseNavMenu);
        } else {
            $("#outer-wrapper").off("click", collapseNavMenu);
        }
    }

    // Nav menu triggers (Desktop/Mobile)
    $("#hamburger-button").on("click", function(e) {
        expandNavMenu(e);
    });

    $(".dropdown-toggle").on("click", function(e) {
        expandNavMenu(e);
    });

});
