<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c"   uri="http://java.sun.com/jsp/jstl/core" %>
<%@taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>뉴스 텍스트 분석 결과 차트</title>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
    	var test = ${boardModel.evaluate }

    	var correct = new Array();
		var all_data = new Array();
		
    	<c:forEach items="${list }" var="BoardModel">
    		correct.push("${BoardModel.correct }");
    	</c:forEach>

    	<c:forEach items="${list }" var="BoardModel">
    		all_data.push("${BoardModel.all_data }");
		</c:forEach>
    	
    	var int_correct = parseInt(correct[0])
    	var int_incorrect = parseInt(all_data[0])-parseInt(correct[0])

      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['correct_or_incorrect', 'count'],
          ['맞힌 갯수',     int_correct],
          ['틀린 갯수',     int_incorrect]
        ]);

        var options = {
          title: '분석 결과'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
      
    </script>
</head>
<body>
	<h1>훈련 결과</h1>
	${BoardModel.correct }
	<div id="piechart" style="width: 900px; height: 500px;"></div>
</body>
</html>