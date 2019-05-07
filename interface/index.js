var jsonFile;
var graphVars = [];

// Load google charts
// bar graph
// pie graph
// scatter graph
// word trees

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
    var options = { 'width':500, 'height':350};

    // Display the chart inside the <div> element with id="piechart"
    var chart = new google.visualization.ScatterChart(document.getElementById('piechart'));
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
      else if (variables[i][1] == "sentence") {
        $(".tree").removeAttr('disabled');
      }
    }
  }

  if(graphVars.length > 0) {
    console.log(graphVars);
    for (var i = 0; i < graphVars.length; i++) {
      if(variables[graphVars[i]][2].length > 1){
        $(".x-axis").append(`<a class="dropdown-item" href="#">${variables[graphVars[i]][0]}</a>`);
        $(".y-axis").append(`<a class="dropdown-item" href="#">${variables[graphVars[i]][0]}</a>`);
      }
      else if (variables[graphVars[i]][1] == "sentence") {
        $(".one-axis").append(`<a class="dropdown-item" href="#">${variables[graphVars[i]][0]}</a>`);
      }
    }
  }
}



function barGraph() {
  $(".tree-options").css({'display': 'none'});
  $(".graph-options").css({'display': 'block'});
}

function pieGraph() {
  $(".tree-options").css({'display': 'none'});
  $(".graph-options").css({'display': 'block'});
}

function scatterGraph() {
  $(".tree-options").css({'display': 'none'});
  $(".graph-options").css({'display': 'block'});
}

function wordGraph() {
  $(".graph-options").css({'display': 'none'});
  $(".tree-options").css({'display': 'block'});
}
