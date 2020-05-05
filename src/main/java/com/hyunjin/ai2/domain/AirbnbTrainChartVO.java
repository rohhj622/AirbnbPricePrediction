package com.hyunjin.ai2.domain;

public class AirbnbTrainChartVO {
	/* *
	 * id
	 * host_id
	 * accommodates
	 * bathrooms
	 * bedrooms
	 * beds
	 * predicted_price
	 * */
	
	private double id; // 분산
	private double price; //표준편차 
	private double predictedPrice; // 평균 
	private double absError; //분석 갯수 루트
	public double getId() {
		return id;
	}
	public void setId(double id) {
		this.id = id;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}
	public double getPredictedPrice() {
		return predictedPrice;
	}
	public void setPredictedPrice(double predictedPrice) {
		this.predictedPrice = predictedPrice;
	}
	public double getAbsError() {
		return absError;
	}
	public void setAbsError(double absError) {
		this.absError = absError;
	}
	
	
}
