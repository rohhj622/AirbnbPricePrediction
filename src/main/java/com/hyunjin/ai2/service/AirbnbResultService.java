package com.hyunjin.ai2.service;

import java.util.List;

import com.hyunjin.ai2.domain.AirbnbResultVO;

public interface AirbnbResultService {
	public List<AirbnbResultVO> selectResult() throws Exception;
}
