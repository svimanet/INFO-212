function markAllBreweries() {
    var mapOptions = {
        center: new google.maps.LatLng(63.5107974, 5.2554845),
        zoom: 5
    }
    var mapCanvas = document.getElementById("map");
    var map = new google.maps.Map(mapCanvas, mapOptions);
    var places = [];
    $.getJSON('/api/brewery/allcoords', function (json) {
            var data = json['results'];
            $.each(data, function(index){
                        var center = new google.maps.LatLng(data[index][0], data[index][1]);
                        var marker = new google.maps.Marker({position: center});
                        marker.setMap(map);
                    })
            });
    }



function searchAddress(address) {
	var geocoder = new google.maps.Geocoder();
    geocoder.geocode(
        {'address': address},
        function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                var loc = results[0].geometry.location;
                var mapOptions = {
				    center: new google.maps.LatLng(loc.lat(), loc.lng()),
				    zoom: 10
				}
				var mapCanvas = document.getElementById("map");
  				var map = new google.maps.Map(mapCanvas, mapOptions);
  				var myCenter = new google.maps.LatLng(loc.lat(), loc.lng());
  				var marker = new google.maps.Marker({position: myCenter});
				marker.setMap(map);
            }
            else {
                alert(address + ", Not found: " + status);
            }
        }
    );
};
