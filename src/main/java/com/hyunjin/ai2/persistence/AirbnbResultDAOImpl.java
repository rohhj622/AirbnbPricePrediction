package com.hyunjin.ai2.persistence;

import java.util.List;

import javax.inject.Inject;

import org.apache.ibatis.session.SqlSession;
import org.springframework.stereotype.Repository;

import com.hyunjin.ai2.domain.AirbnbResultVO;
import com.hyunjin.ai2.domain.AirbnbStatisticsVO;
import com.hyunjin.ai2.domain.AirbnbTrainChartVO;

@Repository
public class AirbnbResultDAOImpl implements AirbnbResultDAO{
	
	@Inject
	SqlSession session;

	private static String namespace = "com.hyunjin.mapper.resultMapper";
	
	@Override
	public List<AirbnbResultVO> selectResult() throws Exception {
		// TODO Auto-generated method stub
		
		return session.selectList(namespace+".selectResult");
	}

	@Override
	public AirbnbStatisticsVO selectStatistics() throws Exception {
		// TODO Auto-generated method stub
		return session.selectOne(namespace+".selectStatistics");
	}

	@Override
	public List<AirbnbTrainChartVO> selectTrainChart() throws Exception {
		// TODO Auto-generated method stub
		return session.selectList(namespace+".selectTrainChart");
	}

}
