// Create Iterable Variable 
var K = 0

// function init(){
//   var selector= d3.select("#selDataset");
//   d3.json("/static/data/samples.json").then((data) => {
//       var sampleNames= data.names;
//       sampleNames.forEach((sample) => {
//           selector
//           .append("option")
//           .text(sample)
//           .property("value", sample);

//       });
// //first chart sample
//       var firstSample= sampleNames[0];
//       buildCharts(firstSample);
//       buildMetadata(firstSample);
//   });
// };

// init();

// ____________________________________
function VisualizeCharts() {
  d3.json("/static/data/samples.json").then(function(data) {
  console.log(data);
  var namesArray= [];
  var metadataArray = [];
  var samplesArray = [];
  var i;
  for (i = 0; i < data.names.length; i++) {
    namesArray.push(data.names[i]);
    metadataArray.push(data.metadata[i]);
    samplesArray.push(data.samples[i]);};
  for (i=0; i <namesArray.length; i++) {
  d3.select("#selDataset").append("option").text(namesArray[i]).property("value", namesArray[i]);
  }
  
  // Call on Chart Formats
  BubbleChartFormat(samplesArray);
  HorizontalBarFormat(samplesArray);
})};
// ____________________________________
function BubbleChartFormat (B) {
var trace1 = {
  x: B[K].otu_ids,
  y: B[K].sample_values,
  mode: 'markers',
  text: B[K].otu_labels,
  marker: {size: B[K].samples_values}
};
var data = [trace1];
var layout = {
    title: 'Marker Size',
    showlegend: false,
    height: 600,
    width: 600,
    xaxis: { title: "OTU ID" }};
Plotly.newPlot('bubble', data, layout);};

// ____________________________________
function HorizontalBarFormat(H) { 
  var trace1 = {
  y: ((H[K].otu_ids).slice(0,10)),
  x: H[K].sample_values.slice(0,10),
  text: ((H[K].otu_ids).slice(0,10)),
  orientation: 'h',
  type: 'bar'};
  var Layout = {
    title: "Top Ten Bacteria",
    margin: {t: 50, l: 250}};
  Plotly.newPlot("bar", trace1, Layout);
  console.log(H[K].sample_values.slice(0,10))
  console.log(((H[K].otu_ids).slice(0,10)))
};

VisualizeCharts();
// var yticks= otu_ids.slice(0,10).map(otuID => `OTU ${otuID}`).reverse();
// var barData= [{
//     y: yticks,
//     x: sample_values.slice(0,10).reverse(),
//     text: otu_labels.slice(0,10).reverse(),
//     orientation: 'h',
//     type: 'bar'
// }];

// var barLayout = {
//     title: "Top 10 Bacteria Cultures Found",
//     margin: {t: 50, l: 150}
// };

// Plotly.newPlot("bar", barData, barLayout);