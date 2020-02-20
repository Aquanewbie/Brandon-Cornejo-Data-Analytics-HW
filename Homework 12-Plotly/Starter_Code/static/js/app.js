// // Create Iterable Variable Based
var K=0
var namesArray= [];
var metadataArray = [];
var samplesArray = [];
// ____________________________________
// Grab Data From JSON and Initiate Plot Functions with JSON Data
function VisualizeCharts() {
  d3.json("/static/data/samples.json").then(function(data) {
  console.log(data);
  var i;
  for (i = 0; i < data.names.length; i++) {
    namesArray.push(data.names[i]);
    metadataArray.push(data.metadata[i]);
    samplesArray.push(data.samples[i]);};
  for (i=0; i <namesArray.length; i++) {
  d3.select("#selDataset").append("option").text(namesArray[i]).property("value", namesArray[i]);
  };
  
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
  marker: {
    size: B[K].sample_values,
    color: B[K].otu_ids,
    colorscale: "Portland"
  }
};
var data = [trace1];
var layout = {
    title: 'Bacteria Cultures per Sample',
    showlegend: false,
    height: 500,
    width: 1000,
    xaxis: { title: "OTU ID" }};
Plotly.newPlot('bubble', data, layout);};

// ____________________________________
function HorizontalBarFormat(H) { 
  var trace1 = [{
  y: H[K].otu_ids.slice(0,10).map(otuID => `OTU ${otuID}`).reverse(),
  x: H[K].sample_values.slice(0,10).reverse(),
  text: (H[K].otu_ids).slice(0,10).reverse(),
  orientation: 'h',
  type: 'bar'}];
  var Layout = {
    title: "Top Ten Bacteria",
    margin: {t: 50, l: 250}};
  Plotly.newPlot("bar", trace1, Layout);
};
// ____________________________________
// Visualize Chart Based on First SampleID (var K = 0)
VisualizeCharts();
// Change the Value of K as New SampleIDs are selected.
// ____________________________________
function optionChanged(value) {
  // Get Index of SampleID from namesArray to Iterate through appended Lists 
  K = namesArray.indexOf(value)
  VisualizeCharts();
};