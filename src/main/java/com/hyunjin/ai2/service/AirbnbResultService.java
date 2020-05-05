package com.hyunjin.ai2.service;

import java.util.List;

import com.hyunjin.ai2.domain.AirbnbResultVO;
import com.hyunjin.ai2.domain.AirbnbStatisticsVO;
import com.hyunjin.ai2.domain.AirbnbTrainChartVO;

public interface AirbnbResultService {
	public List<AirbnbResultVO> selectResult() throws Exception;
	public AirbnbStatisticsVO selectStatistics() throws Exception;
	public List<AirbnbTrainChartVO> selectTrainChart() throws Exception;
}
