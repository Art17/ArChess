/**
 * Created by Artem on 11/26/2016.
 */
jQuery(document).ready(function($) {
    $(".clickable-row").click(function(e) {
        window.document.location = $(this).data("href");
        return true;
    });
});