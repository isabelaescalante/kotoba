var jsonFile;

// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
    var data = google.visualization.arrayToDataTable([
    ['Words', 'Frequency'],
    ['The', 8],
    ['dog', 2],
    ['is', 4],
    ['running', 2],
  ]);

    // Optional; add a title and set the width and height of the chart
    var options = {'title':'', 'width':500, 'height':350};

    // Display the chart inside the <div> element with id="piechart"
    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
}

function readFiles() {
  var file = $("#file-upload")[0].files[0];
  console.log(file.name);
  $(".file-info").html(`${file.name}`);
}

function readFiles(event) {
    var fileList = event.target.files;

    for(var i=0; i < fileList.length; i++ ) {
        loadAsText(fileList[i]);
    }
}

function loadAsText(theFile) {
    var reader = new FileReader();

    reader.onload = function(loadedEvent) {
        // result contains loaded file.
        jsonFile = JSON.parse(loadedEvent.target.result);
        addCompilationResult();
    }
    reader.readAsText(theFile);
}

function addCompilationResult() {
  code = jsonFile.code;
  input = jsonFile.input;
  output = jsonFile.output;
  variables = jsonFile.variables;
  $("#code").val(code);
  if(input.length == 0) {
    $("#inputTA").val("");
  }
  else {
    for (var i = 0; i < input.length; i++) {
      $("#inputTA").append(input[i]);
    }
  }
  if(output.length == 0) {
    $("#outputTA").val("");
  }
  else {
    for (var i = 0; i < output.length; i++) {
      $("#outputTA").append(output[i]);
    }
  }

}
