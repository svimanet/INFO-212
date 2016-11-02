/**
 * Created by goat on 01/11/16.
 */

$(function() {
    $("#searchField").autocomplete({
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
                        // alert("Name:" + sd[0] + "\n"+
                        //       "Address:" + sd[1] + "\n"+
                        //       "Type:" + sd[2] +"\n");
                        searchAddress(sd[1])
                    }
                 });
            });
            //console.log(ui.item.value);
        }
    });
})


