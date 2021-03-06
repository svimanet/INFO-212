var map;
/**
 * Returns a new map if the existing
 * one is not already set.
 */
function getMap(){
    if(!map){
        var mapOptions = {
            center: new google.maps.LatLng(63.5107974, 5.2554845),
            zoom: 5
        }
        var mapCanvas = document.getElementById("map");
        newMap = new google.maps.Map(mapCanvas, mapOptions);
        map = newMap;
        return newMap;
        }
    return map;
}

/**
 * Queries the api for brewery info
 * and places all the markers with info on the map.
 */
function markAllBreweries() {

var map = getMap()
$.getJSON('/api/brewery/allcoords', function (json) {
        var data = json['breweries'];
        $.each(data, function(index){
                    var center = new google.maps.LatLng(data[index]['latitude'], data[index]['longitude']);
                    var marker = new google.maps.Marker({position: center});
                    marker.setMap(map);

                    var infowindow = new google.maps.InfoWindow({
                      content:"<p class='mapmarker'>Name: " + data[index]['name'] + "</p>" +
                              "<p class='mapmarker'>Address: " + data[index]['address'] + "</p>" +
                              "<p class='mapmarker'>Type: " + data[index]['type']  + "</p>"
            });

            google.maps.event.addListener(marker, 'click', function() {
              infowindow.open(map,marker);
            });
        })
    });
}


/**
 * Queries the api for an address and checks google's
 * api for geocodes and changes center if results are found.
 * @param {String} address - The address to search for.
 */
function searchAddress(address) {
var map = getMap()
	var geocoder = new google.maps.Geocoder();
    geocoder.geocode(
        {'address': address},
        function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                var loc = results[0].geometry.location;
                var lat = parseFloat(loc.lat())
                var lng = parseFloat(loc.lng())
                var center = new google.maps.LatLng(lat, lng)
                map.setCenter(center)
                map.setZoom(12)
            }
            else {
                alert(address + ", Not found: " + status);
            }
        }
    );
};

/**
* This method searches the api for a
* brewery, but uses the search inputfield's
* data and not the autocomplete.
*/
function searchAddressFromInput(){
var map = getMap()
var input = document.getElementById('search-field').value
$(document).ready(function() {
            $.ajax({
                type: "GET",
                url: "/api/brewery/name/" + input,
                dataType: "text",
                success: function(data) {
                    var sd = data.split(",")
                    searchAddress(sd[1])
                }
             });
        }
    );
};


function removeDefaultValue(){
    document.getElementById('search-field').value = ""
}

/**
 * Skrevet av kanditat 141.
 */

function show_menu(){
    var mobile_nav = $(".menu-list");
    if(mobile_nav.hasClass('open')){
        mobile_nav.removeClass('open');
        mobile_nav.css('right','-200px');
    }else{
        mobile_nav.addClass('open');
        mobile_nav.css('right','0');
    }
}







