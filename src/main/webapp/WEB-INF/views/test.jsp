<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page session="false" %>
<!DOCTYPE html>
<html>
<head>
<title>AIRBNB Result</title>
<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">	
	<!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">	
	<!-- Latest compiled and minified JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>  
    
    <style type="text/css">		
		div{
			text-align: center;

		}		
		a:link { color: black; text-decoration: none;text-align: center;}
		a:visited { color: black; text-decoration: none;text-align: center;}
		a:hover { color: #595959; text-decoration: none;text-align: center;}	
		
	</style>
	<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
	
	<c:set var="resultSum" value="0"/>    
	<c:set var="i" value="0"/>
	
    <c:forEach items="${resultList}" var="result" varStatus="st">
    	<c:set var="resultSum" value="${resultSum+result.predicted_price}"/>
    	<c:set var="i" value="${i+1}"/>
    </c:forEach>
 
    <c:set var="sumAverage" value="${resultSum/i}"/>
	
  	<script type="text/javascript">
    	google.charts.load("current", {packages:['corechart']});
    	google.charts.setOnLoadCallback(drawChart);
    	function drawChart() {
      	var data = google.visualization.arrayToDataTable([
      		["id", "예측가격", { role: "style" } ],
	        <c:forEach items="${resultList}" var="result" varStatus="st">
          	['${result.id}', parseInt('${result.predicted_price}'),"#99d6ff"],
          	</c:forEach>
      	]);

      	var view = new google.visualization.DataView(data);
     	view.setColumns([0, 1,
        	               { calc: "stringify",
            	             sourceColumn: 1,
                	         type: "string",
                    	     role: "annotation" },
                       	2]);

      	var options = {
        	title: "가격예측",
        	width: 1300,
        	height: 400,
        	bar: {groupWidth: "80%"},
        	legend: { position: "none" },
      	};
      	var chart = new google.visualization.ColumnChart(document.getElementById("columnchart_values"));
      	chart.draw(view, options);
  		}
  	</script>
	<script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawVisualization);

      function drawVisualization() {
        // Some raw data (not necessarily accurate)
        var data = google.visualization.arrayToDataTable([
        	["숙소 id", "예측가격(단위:$)", "평균가격(단위:$)" ],
	        <c:forEach items="${resultList}" var="result" varStatus="st">
          	['${result.id}', parseInt('${result.predicted_price}'),parseInt('${sumAverage}')],
          	</c:forEach>
        ]);

        var options = {
          title : 'Airbnb 가격 예측',
          vAxis: {title: '예측가격(단위:$)'},
          hAxis: {title: '숙소 id'},
          seriesType: 'bars',
          series: {1: {type: 'line'}}        };

        var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
	
</head>
<body>
	<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>

    <div class="container">
    	<div class="row">
    		<div class="col-lg-12">
    			<h1>RESULT</h1>
    		</div>
    	</div>
    	<!-- <div class="row">
    		<div class="col-lg-12">
    			<div id="columnchart_values" style="width: 900px; height: 300px;"></div>
    		</div>
    	</div> -->
    	<div class="row">
    		<div class="col-lg-12">
	    		<div id="chart_div" style="width: 900px; height: 500px;"></div>
    		</div>
    	</div>
    </div>
    
    
</body>
</html>