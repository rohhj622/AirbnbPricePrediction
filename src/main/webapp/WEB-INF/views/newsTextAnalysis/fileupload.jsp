<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c"   uri="http://java.sun.com/jsp/jstl/core" %>
<%@taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>뉴스 텍스트 분석</title>

<script src="//code.jquery.com/jquery-3.3.1.min.js"></script>
<script>
	$(document).ready(function(){
	    //현재HTML문서가 브라우저에 로딩이 끝났다면 
	    $("#analysis").hide();   
	      $('#hideBt').click(function(){
	          $("div").hide();
	          $("#analysis").show();
	          $("#select").attr('disabled',true);
	          $("#upload").attr('disabled',true);
	      });//click
	          
	 });
	function Alert(){
		alert('분석 시 다소 시간이 걸립니다.')
	}
</script>
</head>
<body>
	<h1>파일 업로드</h1>
	
	<form action="fileupload" method="post" enctype="multipart/form-data">
	    <input type="file" name="uploadfile" placeholder="파일 선택" id="select"/>
	    <br/>
	    <input type="submit" value="업로드" id="upload">
	</form>
	<!-- <input type="button" value="분석" onclick="Analysis()"> -->
	<%-- <%=request.getAttribute("fileName")+"  업로드 완료" %> --%>
	<%
		if(request.getAttribute("fileName")==null || request.getAttribute("fileName").toString()==""){
			%><h1>파일을 먼저 선택해주세요.</h1><%
		}
		else{
			String fileName = request.getAttribute("fileName").toString();
			%><%=fileName%> 업로드 완료
				<br>
				<!-- <form action="/Analysis">
					<input type="submit" value="분석" class="button">
				</form> -->
				<!-- <input type="button" value="분석" onclick="Analysis()"> -->
				<!-- <input type="button" onclick="Analysis()" value="분석">  -->
				<br>
				<form action="Analysis" method="post">
				    <div><input type="submit" value="분석" onclick="Alert();" id="hideBt"></div>
				</form>
				
				<h1 id="analysis">분석 중 입니다... 잠시만 기다려 주세요.</h1>
				
			<%
		}
	%>
</body>
</html>