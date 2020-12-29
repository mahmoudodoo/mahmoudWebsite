       google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);
  
        function drawChart() {
  
          var data = google.visualization.arrayToDataTable([
            ['Task', 'Hours per Day'],
            ['Used',  parseInt(document.getElementById('used_disk').textContent)],
            ['Free',  parseInt(document.getElementById('free_disk').textContent)]
          ]);
  
          var options = {
            title: 'Disk',
            pieHole: 1,
            tooltip: { isHtml: true },
          };
  
          var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  
          chart.draw(data, options);
        }