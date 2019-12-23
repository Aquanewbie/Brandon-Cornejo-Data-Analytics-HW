// Get a reference to the table body
var tbody = d3.select("tbody");

// Console.log the weather data from data.js
console.log(data);

// // Step 1: Loop Through `data` and console.log each ufoSighting object
data.forEach(function(ufoSighting) {
  console.log(ufoSighting);
});

// // Step 2:  Use d3 to append one table row `tr` for each ufoSighting object
// // Don't worry about adding cells or text yet, just try appending the `tr` elements.
data.forEach(function(ufoSighting) {
  console.log(ufoSighting);
  var row = tbody.append("tr");
});

// // Step 3:  Use `Object.entries` to console.log each weather report value
data.forEach(function(ufoSighting) {
  console.log(ufoSighting);
  var row = tbody.append("tr");

  Object.entries(ufoSighting).forEach(function([key, value]) {
    console.log(key, value);
  });
});

// // Step 4: Use d3 to append 1 cell per ufoSighting value (weekday, date, high, low)
data.forEach(function(ufoSighting) {
  console.log(ufoSighting);
  var row = tbody.append("tr");

  Object.entries(ufoSighting).forEach(function([key, value]) {
    console.log(key, value);
    // Append a cell to the row for each value
    // in the weather report object
    var cell = row.append("td");
  });
});

// // Step 5: Use d3 to update each cell's text with
// // ufoSighting values (weekday, date, high, low)
data.forEach(function(ufoSighting) {
  console.log(ufoSighting);
  var row = tbody.append("tr");
  Object.entries(ufoSighting).forEach(function([key, value]) {
    console.log(key, value);
    // Append a cell to the row for each value
    // in the weather report object
    var cell = row.append("td");
    cell.text(value);
  });
});

// BONUS: Refactor to use Arrow Functions!
data.forEach((ufoSighting) => {
  var row = tbody.append("tr");
  Object.entries(ufoSighting).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
  });
});