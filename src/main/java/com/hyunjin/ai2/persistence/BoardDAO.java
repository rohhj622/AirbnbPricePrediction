package com.hyunjin.ai2.persistence;

import java.util.List;

import com.hyunjin.ai2.domain.BoardModel;;

public interface BoardDAO {
	//VO를 가지고 실제로 접근하는 애
	//물리적
	//mapper까지 가게해줌
	
	public List<BoardModel> list(BoardModel board)throws Exception;
}
