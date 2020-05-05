package com.hyunjin.ai2.persistence;

import java.util.List;

import com.hyunjin.ai2.domain.AirbnbResultVO;
import com.hyunjin.ai2.domain.AirbnbStatisticsVO;
import com.hyunjin.ai2.domain.AirbnbTrainChartVO;

public interface AirbnbResultDAO {
	List<AirbnbResultVO> selectResult() throws Exception;
	AirbnbStatisticsVO selectStatistics() throws Exception;
	List<AirbnbTrainChartVO> selectTrainChart() throws Exception;
}
