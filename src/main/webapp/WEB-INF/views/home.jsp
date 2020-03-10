<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page session="false" %>
<html>
<head>
	<script src="//code.jquery.com/jquery-1.10.2.js"></script>
    <script src="//code.jquery.com/ui/1.11.0/jquery-ui.js"></script>
	<title>Home</title>
</head>
<body>

<h1>
	Hello world! 
</h1>


<h1>파일 업로드</h1>

<form action="fileupload" method="post" enctype="multipart/form-data">
	<select name="country">
		<option value="airbnb_assets" selected="selected">해당없음</option>
		<option value="airbnb_US">United States</option>
	</select>
	<br>
    <input type="file" name="uploadfile" placeholder="파일 선택" /><br/>
    <input type="submit" value="업로드">
</form>
<!-- 	  	<option value="파인애플">Athens, Attica, Greece</option>
	  	<option value="파인애플">Barcelona, Catalonia, Spain</option>
	  	<option value="파인애플">Barossa Valley, South Australia, Australia</option>
	  	<option value="파인애플">Barwon South West, Vic, Victoria, Australia</option>
	  	<option value="파인애플">Belize, Belize, Belize</option>
	  	<option value="파인애플">Berlin, Berlin, Germany</option>
	  	<option value="파인애플">Bergamo, Lombardia, Italy</option>
	  	<option value="파인애플">Bologna, Emilia-Romagna, Italy</option>
	  	<option value="파인애플">Bordeaux, Nouvelle-Aquitaine, France</option> -->
	  	
</body>
</html>
