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

$(document).ready(function() {
  $("#run_code").on('click', function() {
    code = $("#code").val();
    if(code == "") {
      alert("Write code to run.");
    }
  });
})


//ajax post request
function post_request_ajax(uri,data_js,result_id){
    $.ajax({
        url: uri,
        type: "POST",
        data: data_js,
        dataType: "json",
        contentType: "application/json",
        success: function (jsonResponse) {
            //alert("success" + jsonResponse.result);
            $(result_id).text(jsonResponse.result);
        },
        error: function (errorMessage) {
            alert("error");

        }
    });
}
