package com.hyunjin.ai2.domain;

public class AirbnbStatisticsVO {
	/* *
	 * id
	 * host_id
	 * accommodates
	 * bathrooms
	 * bedrooms
	 * beds
	 * predicted_price
	 * */
	
	private double var; // 분산
	private double std; //표준편차 
	private double mean; // 평균 
	private double numsqrt; //분석 갯수 루트
	
	public double getVar() {
		return var;
	}
	public void setVar(double var) {
		this.var = var;
	}
	public double getStd() {
		return std;
	}
	public void setStd(double std) {
		this.std = std;
	}
	public double getMean() {
		return mean;
	}
	public void setMean(double mean) {
		this.mean = mean;
	}
	public double getNumsqrt() {
		return numsqrt;
	}
	public void setNumsqrt(double numsqrt) {
		this.numsqrt = numsqrt;
	}
	
}
