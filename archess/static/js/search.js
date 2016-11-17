/**
 * Created by Artem on 12/3/2016.
 */


function addScripts() {
        $(".clickable-row").click(function(e) {
    window.document.location = $(this).data("href");
    return true;
    });
}

function instantSearch() {
    var ajaxRequest;
    ajaxRequest = new XMLHttpRequest();
    ajaxRequest.onreadystatechange = function() {
        if(ajaxRequest.readyState == 4 && ajaxRequest.status == 200) {
            console.log('hello')
            var template = $("#table_template").html();
            var all = JSON.parse(ajaxRequest.responseText);
            console.log('hello')
            if(!all.length) {
                if(!$('#id_search_error').length)
                    $('#id_author').after('<span id="id_search_error" class="error text-warning">Nothing found</span>')
                $('#template_div').html('');
                $('#pagination').hide()
            }
            else {
                $('#id_search_error').remove();

                var pagination_selector = $('#pagination');
                pagination_selector.show();
                pagination_selector.pagination({
                dataSource: all,
                pageSize: 4,
                autoHidePrevious: true,
                autoHideNext: true,
                    ulClassName: 'pagination',
                callback: function(data, pagination) {
                    var dict = {
                        'tasks': data
                    };
                html = Mustache.render(template, dict);
                $('#template_div').html(html);
                    addScripts();
                }
            })
            }
        }
    };
    ajaxRequest.open('GET', '/api/tasks/?format=json&name='+ $('#id_author').val() );
    ajaxRequest.send()
}

$(document).ready(function() {
    instantSearch();
    $('#id_author').on('input', instantSearch);
});