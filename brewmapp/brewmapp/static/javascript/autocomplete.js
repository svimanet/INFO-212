/**
 * Created by goat on 01/11/16.
 */

/**
* This method queries the api for possible
* breweries and suggests autocompletions for the
* users. If a suggestion is used, the searchAddress
* function is executed.
*/
$(function() {
    $("#search-field").autocomplete({
        source:function(request, response) {
            $.getJSON("/api/brewery/search/" + request.term,{
            }, function(data) {
                response(data.results);
            });
        },
        minLength: 2,
        select: function(event, ui) {
            $(document).ready(function() {
                $.ajax({
                    type: "GET",
                    url: "/api/brewery/name/" + ui.item.value,
                    dataType: "text",
                    success: function(data) {
                        var sd = data.split(",")
                        searchAddress(sd[1])
                    }
                 });
            });
        }
    });
});


