<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>

<script src="//code.jquery.com/jquery-3.3.1.min.js"></script>
<script>
	$(document).ready(function(){
	    //현재HTML문서가 브라우저에 로딩이 끝났다면 
	    $("#test").hide();  
	      $('#showBt').click(function(){
	          $("div").hide();
	          $("#dis").attr('disabled',true);
	      });//click
	          
	       $('#hideBt').click(function(){
	          $("#test").show();
	                   });
	 });
</script>
</head>
<body>
	<div>안녕, jQuery~
	<button id="showBt">숨기기</button></div>
	<button id="hideBt" >보이기</button>
	<button id="dis" >button</button>
	<h1 id="test">test</h1>
</body>
</html>