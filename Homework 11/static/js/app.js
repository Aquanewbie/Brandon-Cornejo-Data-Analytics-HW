// Populate Table with ufoSighting Data
function populatewholetable(data){
  // Remove Old Cell Data
    d3.selectAll("td").remove(); 
    data.forEach((ufoSighting) => {
      var row = d3.select("tbody").append("tr");
      console.log(ufoSighting);
      Object.entries(ufoSighting).forEach(([key, value]) => {
        var cell = row.append("td");
        cell.text(value);
        console.log(key, value);
      });
    });
}
// Use d3 to Retrieve User Input 
function populatetablefiltered() {
  var dateTime1 = d3.select("#datetime").property("value");
  var filteredData = data
  console.log(dateTime1);
  // Update filteredData with filtered data
  if (dateTime1) {
    filteredData = data.filter(row => row.datetime === dateTime1);
    if (filteredData.length !== 0){
      console.log(filteredData);
    }
    else (window.alert("There were no recorded signtings for given date."))
  }
  populatewholetable(filteredData);

}

// Event Listener for Button Click
d3.selectAll("#filter-btn").on("click", populatetablefiltered);

// Initiate Function 
populatewholetable(data);




