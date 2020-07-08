# AirbnbPricePrediction
> 에어비앤비 숙소의 가격을 예측해주는 웹사이트입니다.
#eclipse #spring #mysql8.0.17 #apacheTomcat9.0.24 #googleChart
#python3 #pandas #k-nearest-neighbor #scikitLearn

## 주요 기능
- **가격 예측**
- **결과 차트로 표현**
### 설명
- 사용 모델
  + k-nearest-neighbor Regression
- 모델 학습 비율
  + **Train 70%, Test 30%**
- 사용한 데이터  
  + id
  + host_id
  + accommodates
  + bathrooms
  + bedrooms
  + beds
  + price

- 사용자가 업로드할 파일의 columns
  + id
  + host_id
  + accommodates
  + bathrooms
  + bedrooms
  + beds

## 스크린샷
- 차트
![image](https://user-images.githubusercontent.com/54883322/76288391-f6753580-62e9-11ea-9d14-42a6ff33af69.png)
- 숙소 id에 따른 숙소 가격
- 평균값은 사용자가 올린 파일의 예측값들의 평균.
- 사용차트 :  google chart
---------------------------------------
> train과 test에 사용한 데이터 출처 : <http://insideairbnb.com/get-the-data.html>

> 참고한 페이지 : <https://velog.io/@leejh3224/Machine-Learning-%EC%97%90%EC%96%B4%EB%B9%84%EC%95%A4%EB%B9%84-%EA%B0%80%EA%B2%A9-%EC%98%88%EC%B8%A1>

> 논문 발표 자료& 발표 영상 : https://drive.google.com/drive/folders/1qg8RGkSfcVny3U8axOmgVvh8VSWtKNP5?usp=sharing
