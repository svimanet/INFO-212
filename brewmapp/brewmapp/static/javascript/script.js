function myMap() {
  var mapCanvas = document.getElementById("map");
  var mapOptions = {
    center: new google.maps.LatLng(60.39126279999999, 5.32205440000007), 
    zoom: 10
  }
  var map = new google.maps.Map(mapCanvas, mapOptions);
  var center = new google.maps.LatLng(60.39126279999999, 5.32205440000007);
  var marker = new google.maps.Marker({position: center});
  marker.setMap(map);
}

/* Should be replaced with searchAddress */
function search() {
	var addressField = document.getElementById('searchField');
	var geocoder = new google.maps.Geocoder();
    geocoder.geocode(
        {'address': addressField.value}, 
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
                alert("Not found: " + status); 
            } 
        }
    );
};


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