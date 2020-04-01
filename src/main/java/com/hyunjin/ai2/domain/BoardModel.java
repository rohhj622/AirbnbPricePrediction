package com.hyunjin.ai2.domain;

import java.util.Date;

public class BoardModel {
	
	private double evaluate;
	private int correct;
	private int all_data;
	public double getEvaluate() {
		return evaluate;
	}
	public void setEvaluate(double evaluate) {
		this.evaluate = evaluate;
	}
	public int getCorrect() {
		return correct;
	}
	public void setCorrect(int correct) {
		this.correct = correct;
	}
	public int getAll_data() {
		return all_data;
	}
	public void setAll_data(int all_data) {
		this.all_data = all_data;
	}

}
