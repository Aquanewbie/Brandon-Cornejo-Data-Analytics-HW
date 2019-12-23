// Get a reference to the table body
var tbody = d3.select("tbody");

// Populate Table with ufoSighting Data!
// Remove Old Cell Data
function populatewholetable(data){
    d3.selectAll("td").remove(); 
    data.forEach((ufoSighting) => {
      var row = tbody.append("tr");
      console.log(ufoSighting);
      Object.entries(ufoSighting).forEach(([key, value]) => {
        var cell = row.append("td");
        cell.text(value);
        console.log(key, value);
      });
    });
}

function populatetablefiltered(data) {
    var dateTime1 = d3.select("#datetime").property("value");
    console.log(dateTime1);

    if (dateTime1) {
   
    filteredData = data.filter(row => row.datetime === dateTime1);
    populatewholetable(filteredData); 
  }
  populatewholetable(data);

}

// Event Listener
d3.selectAll("#filter-btn").on("click", populatetablefiltered);

// Initiate Function 
populatewholetable(data);




