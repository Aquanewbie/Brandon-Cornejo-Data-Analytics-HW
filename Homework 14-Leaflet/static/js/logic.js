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

var colorrange = d3.scaleLinear().domain([4.5,6.5]).range(['#FFFF00', '#ff0000'])
var MarkerRadius = d3.scaleLinear().domain([4.5,6.5]).range([5, 20])

d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson", function(data) {

    // Run through a Magnitude of Colors
    function magnitudecolors (value) {
        return (colorrange(value))};

    L.geoJson(data, {
        style: function(feature) {
            return { color: magnitudecolors(feature.properties.mag)
            };
        },
        pointToLayer: function(feature, latlng) {
            return new L.CircleMarker(latlng, {
                radius: MarkerRadius(feature.properties.mag), 
                fillOpacity: 1
            });
        },
        onEachFeature: function (feature, layer) {
            layer.bindPopup("Title: " + feature.properties.title + "<br>" + "Magnitude: " + feature.properties.mag );
        }
    }).addTo(EarthquakeMap)});



var legend = L.control({position: 'bottomright'});

legend.onAdd = function (map) {
    
var div = L.DomUtil.create('div', 'info legend'),
    grades = [4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0],
    labels = [];
var LegendColorRange = d3.scaleLinear().domain([4.5,6.5]).range(['#FFFF00', '#ff0000'])
// loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + LegendColorRange(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }
    
    return div;
    };

legend.addTo(EarthquakeMap)