// Creating map object
var EarthquakeMap = L.map("map", {
  center: [22.8515625,
    27.68352808378776],
    minzoom:1,
  zoom: 2,
  maxZoom: 5
});

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(EarthquakeMap);



d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson", function(data) {
    console.log(data[0]);
    
    L.geoJson(data, {
        style: function(feature) {
            return {
                color: "green"
            };
        },
        pointToLayer: function(feature, latlng) {
            return new L.CircleMarker(latlng, {
                radius: 10, 
                fillOpacity: 0.85
            });
        },
        onEachFeature: function (feature, layer) {
            layer.bindPopup(feature.properties.NAME);
        }
    }).addTo(EarthquakeMap)});

// var greenIcon = L.icon({
//     iconUrl: 'leaf-green.png',
//     shadowUrl: 'leaf-shadow.png',
    
//     iconSize:     [38, 95], // size of the icon
//     shadowSize:   [50, 64], // size of the shadow
//     iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
//     shadowAnchor: [4, 62],  // the same for the shadow
//     popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
//     });

// // Typical Magnitudes ranges -1,0,1,2,3,4,5,6,7,8,9,10
// var color = d3.scale.linear().domain([Magmin,Magmax])
//         .range(['#FFFF00', '#FF0000']);