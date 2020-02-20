// Step 1: Set up our chart
//= ================================
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 50
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Step 2: Create an SVG wrapper,
// append an SVG group that will hold our chart,
// and shift the latter by left and top margins.
// =================================
var svg = d3
  .select("body")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Step 3:
// Import data from the donuts.csv file
// =================================
d3.csv("assets/data/data.csv").then(function(DataData) {
  // Step 4: Parse the data

  // Format the data
  DataData.forEach(function(data) {
    data.date = parseTime(data.date);
    data.morning = +data.morning;
    data.evening = +data.evening;
  });

  // Step 5: Create Scales
  //= ============================================
  var xTimeScale = d3.scaleTime()
    .domain(d3.extent(donutData, d => d.date))
    .range([0, width]);

  var yLinearScale1 = d3.scaleLinear()
    .domain([0, d3.max(donutData, d => d.morning)])
    .range([height, 0]);

  var yLinearScale2 = d3.scaleLinear()
    .domain([0, d3.max(donutData, d => d.evening)])
    .range([height, 0]);

  // Step 6: Create Axes
  // =============================================
  var bottomAxis = d3.axisBottom(xTimeScale).tickFormat(d3.timeFormat("%d-%b"));
  var leftAxis = d3.axisLeft(yLinearScale1);
  var rightAxis = d3.axisRight(yLinearScale2);


  // Step 7: Append the axes to the chartGroup
  // ==============================================
  // Add bottomAxis
  chartGroup.append("g").attr("transform", `translate(0, ${height})`).call(bottomAxis);

  // Add leftAxis to the left side of the display
  chartGroup.append("g").call(leftAxis);

  // Add rightAxis to the right side of the display
  chartGroup.append("g").attr("transform", `translate(${width}, 0)`).call(rightAxis);


  // Step 8: Set up two line generators and append two SVG paths
  // ==============================================
  // Line generators for each line
  var line1 = d3
    .line()
    .x(d => xTimeScale(d.date))
    .y(d => yLinearScale1(d.morning));

  var line2 = d3
    .line()
    .x(d => xTimeScale(d.date))
    .y(d => yLinearScale2(d.evening));


  // Append a path for line1
  chartGroup.append("path")
    .data([donutData])
    .attr("d", line1)
    .classed("line green", true);

  // Append a path for line2
  chartGroup.append("path")
    .data([donutData])
    .attr("d", line2)
    .classed("line orange", true);

}).catch(function(error) {
  console.log(error);
});

_______________________



var svg= d3.select("#scatter").append("svg").attr("width" , chartWidth).attr("height",chartHeight);
console.log(d3.csv("assets/data/data.csv"))

// // @TODO: YOUR CODE HERE!
// d3.csv("assets/data/data.csv").then(function(data){
//     var i;
//     for (i = 0; i < data.length; i++) {
//         console.log(data[i].smokes)
//         svg.append("circle").attr("cx", data[i].smokes).attr("cy", data[i].poverty).attr("r", 5).style("fill", "pink");
//     }
// })

// svg container
var svgHeight = 400;
var svgWidth = 1000;

// margins
var margin = {
  top: 50,
  right: 50,
  bottom: 50,
  left: 50
};

// chart area minus margins
var chartHeight = svgHeight - margin.top - margin.bottom;
var chartWidth = svgWidth - margin.left - margin.right;

// shift everything over by the margins
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// scale y to chart height
var yScale = d3.scaleLinear()
  .domain([0, d3.max(d3.csv("assets/data/data.csv"))])
  .range([chartHeight, 0]);

// scale x to chart width
var xScale = d3.scaleBand()
  .domain(d3.csv("assets/data/data.csv"))
  .range([0, chartWidth])
  .padding(0.05);

// create axes
var yAxis = d3.axisLeft(yScale);
var xAxis = d3.axisBottom(xScale);

// set x to the bottom of the chart
chartGroup.append("g")
  .attr("transform", `translate(0, ${chartHeight})`)
  .call(xAxis);

// set y to the y axis
// This syntax allows us to call the axis function
// and pass in the selector without breaking the chaining
chartGroup.append("g")
  .call(yAxis);

// @TODO: YOUR CODE HERE!
d3.csv("assets/data/data.csv").then(function(data){
    var i;
    for (i = 0; i < data.length; i++) {
        console.log(data[i].smokes)
        chartGroup.append("circle").attr("cx", data[i].smokes).attr("cy", data[i].poverty).attr("r", 5).style("fill", "pink");
    }
})





// svgContainer.selectAll("circle").data(DataData).enter().append("circle")
// function appendCircle(DataVariable) {
//     // svgContainer.append("circle").attr("cx", 25).attr("cy", 25).attr("r", 25).style("fill", "purple")
//     var i;
//     for (i = 0; i < DataVariable.length; i++) {
//         svgContainer.append("circle").attr("cx", i.smokes).attr("cy", i.smokes).attr("r", 4).style("fill", "pink");}
// };

// appendCircle(DataData);

// var i;
// for (i = 0; i < DataData.length; i++) {
//     svgContainer.append("circle").attr("cx", i.smokes).attr("cy", i.smokes).attr("r", 4).style("fill", "pink");
// }

// console.log(DataData[5])