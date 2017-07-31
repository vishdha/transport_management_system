// Copyright (c) 2017, Vishal Dhayagude and contributors
// For license information, please see license.txt

frappe.ui.form.on('Location Data Calculation', {
	refresh: function(frm) {

	}
});



// Created By Seng on 23/08/2016
// Please do use this script at your own risk, feel free to do your own customization as needed.

frappe.ui.form.on("Location Data Calculation", "load_this", function(frm){ // Replace Employee to your formtype, load_this to your button name
    // set your origin address, accepts LatLng | String | google.maps.Place
    // destination address getting from the form, replace permanent_address to your field name
    // Refer API for more info https://developers.google.com/maps/documentation/javascript/directions
    console.log("inside");
    var originAddress = frm.doc.source_address;
    var destAddress = frm.doc.destination_address;
    console.log("inside",originAddress,destAddress);
    initMap(originAddress, destAddress);
});

frappe.ui.form.on("Location Data Calculation", "load_api", function(frm){
    function initialize() {
    var input = document.getElementById('location');
    var autocomplete = new google.maps.places.Autocomplete(input);
    }

    google.maps.event.addDomListener(window, 'load', initialize);
});

function initMap(originAddress, destAddress) {
  // Initiate map with the origin address

  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: originAddress,
  });
  directionsDisplay.setMap(map);

    calculateAndDisplayRoute(directionsService, directionsDisplay, originAddress, destAddress);
}

function calculateAndDisplayRoute(directionsService, directionsDisplay, originAddress, destAddress) {
  // For more customization on the route and distanceMatrix, please refer to the API
  // API Link: https://developers.google.com/maps/documentation/javascript/distancematrix

  var service = new google.maps.DistanceMatrixService();
  directionsService.route({
    origin: originAddress,
    destination: destAddress,
    travelMode: google.maps.TravelMode.DRIVING
  }, function(response, status) {
    if (status === google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(response);
    } else {
      window.alert('Directions request failed due to ' + status); // Customize your own error here
    }
  });


    service.getDistanceMatrix({
        origins: [originAddress],
        destinations: [destAddress],
        travelMode: google.maps.TravelMode.DRIVING,
        unitSystem: google.maps.UnitSystem.METRIC,
        avoidHighways: false,
        avoidTolls: false
    }, function (response, status) {
        if (status == google.maps.DistanceMatrixStatus.OK && response.rows[0].elements[0].status != "ZERO_RESULTS") {
            var distance = response.rows[0].elements[0].distance.text;

            // Display the distance in an form input, replace distance2 as your field name
            cur_frm.set_value("distance_map", distance);

            // The following line display to external div id instead of form input
            // Create an HTML field with the following option:
            // <p>Total Distance between two location:<span id="total"></span></p>

            // Uncomment the next 3 line to show the result in external div id
            var dvDistance = document.getElementById("total");
            dvDistance.innerHTML = "";
            dvDistance.innerHTML += " "+distance;

        } else {
            alert("Unable To Find Distance Via Road.");
        }
    });

}