package com.hyunjin.ai2.service;

import java.util.List;

import javax.inject.Inject;

import org.springframework.stereotype.Service;

import com.hyunjin.ai2.domain.AirbnbResultVO;
import com.hyunjin.ai2.domain.AirbnbStatisticsVO;
import com.hyunjin.ai2.domain.AirbnbTrainChartVO;
import com.hyunjin.ai2.persistence.AirbnbResultDAO;

@Service
public class AirbnbResultServiceImpl implements AirbnbResultService {
	
	@Inject
	AirbnbResultDAO dao;

	@Override
	public List<AirbnbResultVO> selectResult() throws Exception {
		// TODO Auto-generated method stub
		return dao.selectResult();
	}

	@Override
	public AirbnbStatisticsVO selectStatistics() throws Exception {
		// TODO Auto-generated method stub
		return dao.selectStatistics();
	}

	@Override
	public List<AirbnbTrainChartVO> selectTrainChart() throws Exception {
		// TODO Auto-generated method stub
		return dao.selectTrainChart();
	}

}
