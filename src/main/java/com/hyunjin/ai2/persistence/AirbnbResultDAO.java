package com.hyunjin.ai2.persistence;

import java.util.List;

import com.hyunjin.ai2.domain.AirbnbResultVO;

public interface AirbnbResultDAO {
	List<AirbnbResultVO> selectResult() throws Exception;
}
