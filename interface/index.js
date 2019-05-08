var jsonFile;
var graphVars = [];
var xName;
var yName;
var xType;
var yType;
var xData = [];
var yData = [];
var graphData = [];
var graphChosen;

// Load google charts
// bar graph
// pie graph
// scatter graph
// word trees

google.charts.load('current', {'packages':['corechart']});
// google.charts.setOnLoadCallback(drawChart);

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
        graphsOn();
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
    $("#inputTA").val("No input");
  }
  else {
    for (var i = 0; i < input.length; i++) {
      $("#inputTA").append(input[i] + "\n");
    }
  }
  if(output.length == 0) {
    $("#outputTA").val("No output");
  }
  else {
    for (var i = 0; i < output.length; i++) {
      $("#outputTA").append(output[i] + "\n");
    }
  }

  if(variables.length > 0) {
    for (var i = 0; i < variables.length; i++) {
      $(".table tr:last").after(`
        <tr>
          <td>${variables[i][0]}</td>
          <td>${variables[i][1]}</td>
          <td>${variables[i][2]}</td>
        </tr>
        `);
    }
  }
}

function graphsOn() {
  variables = jsonFile.variables;
  data = '';
  for (var i = 0; i < variables.length; i++) {
    if($.isArray(variables[i][2])) {
      // data = JSON.parse(`{
      //   "varName" : "${variables[i][0]}",
      //   "varIndexVal" : ${variables[i][2]}
      // }`);
      // console.log(data)
      graphVars.push(i);
      if(graphVars.length > 1) {
        $(".scatter").removeAttr('disabled');
        $(".pie").removeAttr('disabled');
        $(".bar").removeAttr('disabled');
      }
    }
  }

  if(graphVars.length > 0) {
    for (var i = 0; i < graphVars.length; i++) {
      if(variables[graphVars[i]][2].length > 1){
        $(".x-axis").append(`<option>${variables[graphVars[i]][0]}</option>`);
        $(".y-axis").append(`<option>${variables[graphVars[i]][0]}</option>`);
      }
    }
  }
}

function barGraph() {
  graphChosen = "bar";
  xData = [];
  yData = [];
  graphData = [];
  $("#sel1Bar").css({'display' : 'block'});
  $("#sel2Bar").css({'display' : 'block'});
  $("#sel1Pie").css({'display' : 'none'});
  $("#sel2Pie").css({'display' : 'none'});
  $("#sel1Scatter").css({'display' : 'none'});
  $("#sel2Scatter").css({'display' : 'none'});
}

function pieGraph() {
  graphChosen = "pie";
  xData = [];
  yData = [];
  graphData = [];
  $("#sel1Pie").css({'display' : 'block'});
  $("#sel2Pie").css({'display' : 'block'});
  $("#sel1Scatter").css({'display' : 'none'});
  $("#sel2Scatter").css({'display' : 'none'});
  $("#sel1Bar").css({'display' : 'none'});
  $("#sel2Bar").css({'display' : 'none'});
}

function scatterGraph() {
  graphChosen = "scatter";
  xData = [];
  yData = [];
  graphData = [];
  $("#sel1Scatter").css({'display' : 'block'});
  $("#sel2Scatter").css({'display' : 'block'});
  $("#sel1Pie").css({'display' : 'none'});
  $("#sel2Pie").css({'display' : 'none'});
  $("#sel1Bar").css({'display' : 'none'});
  $("#sel2Bar").css({'display' : 'none'});
}

document.getElementById("sel1Bar").addEventListener("change", getBarGraphValues);
document.getElementById("sel2Bar").addEventListener("change", getBarGraphValues);

function getBarGraphValues() {
  var x = document.getElementById("sel1Bar").value;
  var y = document.getElementById("sel2Bar").value;
  if(x != "x-axis" && y != "y-axis") {
    for (var i = 0; i < graphVars.length; i++) {
      if(x == variables[graphVars[i]][0]) {
        xName = variables[graphVars[i]][0];
        xType = variables[graphVars[i]][1];
        xData = variables[graphVars[i]][2];
      }
      else if (y == variables[graphVars[i]][0]) {
        yName = variables[graphVars[i]][0];
        yType = variables[graphVars[i]][1];
        yData = variables[graphVars[i]][2];
      }
    }

    if (xData.length == yData.length) {
      for (var i = 0; i < xData.length; i++) {
        xVar = xData[i].replace(/"/g, "");
        yVar = yData[i].replace(/"/g, "");
        graphData.push([xVar, yVar]);
      }
    }
    else {
      alert("Error: variables have to be the same size");
    }

    createGraph();
    $(".form-inline").trigger("reset");
  }
}

document.getElementById("sel1Pie").addEventListener("change", getPieGraphValues);
document.getElementById("sel2Pie").addEventListener("change", getPieGraphValues);

function getPieGraphValues() {
  var x = document.getElementById("sel1Pie").value;
  var y = document.getElementById("sel2Pie").value;
  if(x != "x-axis" && y != "y-axis") {
    for (var i = 0; i < graphVars.length; i++) {
      if(x == variables[graphVars[i]][0]) {
        xName = variables[graphVars[i]][0];
        xType = variables[graphVars[i]][1];
        xData = variables[graphVars[i]][2];
      }
      else if (y == variables[graphVars[i]][0]) {
        yName = variables[graphVars[i]][0];
        yType = variables[graphVars[i]][1];
        yData = variables[graphVars[i]][2];
      }
    }

    if (xData.length == yData.length) {
      for (var i = 0; i < xData.length; i++) {
        xVar = xData[i].replace(/"/g, "");
        yVar = yData[i].replace(/"/g, "");
        graphData.push([xVar, yVar]);
      }
    }
    else {
      alert("Error: variables have to be the same size");
    }

    createGraph();
    $(".form-inline").trigger("reset");
  }
}

document.getElementById("sel1Scatter").addEventListener("change", getScatterGraphValues);
document.getElementById("sel2Scatter").addEventListener("change", getScatterGraphValues);

function getScatterGraphValues() {
  var x = document.getElementById("sel1Scatter").value;
  var y = document.getElementById("sel2Scatter").value;
  if(x != "x-axis" && y != "y-axis") {
    for (var i = 0; i < graphVars.length; i++) {
      if(x == variables[graphVars[i]][0]) {
        xName = variables[graphVars[i]][0];
        xType = variables[graphVars[i]][1];
        xData = variables[graphVars[i]][2];
      }
      else if (y == variables[graphVars[i]][0]) {
        yName = variables[graphVars[i]][0];
        yType = variables[graphVars[i]][1];
        yData = variables[graphVars[i]][2];
      }
    }

    if (xData.length == yData.length) {
      for (var i = 0; i < xData.length; i++) {
        xVar = xData[i].replace(/"/g, "");
        yVar = yData[i].replace(/"/g, "");
        graphData.push([xVar, yVar]);
      }
    }
    else {
      alert("Error: variables have to be the same size");
    }

    createGraph();
    $(".form-inline").trigger("reset");
  }
}

function createGraph() {
  finalData = [];

  if(graphChosen == "bar") {
    $("#piechart").css({'display' : 'none'});
    $("#piechart").empty();
    $("#scatterchart").css({'display' : 'none'});
    $("#scatterchart").empty();

    finalData.push([xName, yName]);
    for (var i = 0; i < graphData.length; i++) {
      if(yType == "number") {
        graphData[i][1] = Number(graphData[i][1]);
      }

      finalData.push(graphData[i]);
    }

    var data = google.visualization.arrayToDataTable(finalData);

    var options = { 'width':500, 'height':350};

    var chart = new google.visualization.BarChart(document.getElementById('barchart'));
    chart.draw(data, options);

    $("#barchart").css({'display' : 'block'});
  }
  else if (graphChosen == "pie") {
    $("#barchart").css({'display' : 'none'});
    $("#barchart").empty();
    $("#scatterchart").css({'display' : 'none'});
    $("#scatterchart").empty();

    finalData.push([xName, yName]);
    for (var i = 0; i < graphData.length; i++) {
      if(yType == "number") {
        graphData[i][1] = Number(graphData[i][1]);
      }

      finalData.push(graphData[i]);
    }

    var data = google.visualization.arrayToDataTable(finalData);

    var options = { 'width':500, 'height':350};

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);

    $("#piechart").css({'display' : 'block'});
  }
  else if (graphChosen == "scatter") {
    $("#barchart").css({'display' : 'none'});
    $("#barchart").empty();
    $("#piechart").css({'display' : 'none'});
    $("#piechart").empty();

    finalData.push([xName, yName]);
    for (var i = 0; i < graphData.length; i++) {
      if(yType == "number") {
        graphData[i][1] = Number(graphData[i][1]);
      }

      finalData.push(graphData[i]);
    }

    var data = google.visualization.arrayToDataTable(finalData);

    var options = { 'width':500, 'height':350};

    var chart = new google.visualization.ScatterChart(document.getElementById('scatterchart'));
    chart.draw(data, options);

    $("#scatterchart").css({'display' : 'block'});
  }
}
