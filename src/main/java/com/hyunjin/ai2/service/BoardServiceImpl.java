package com.hyunjin.ai2.service;

import java.util.List;

import javax.inject.Inject;

import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;

import com.hyunjin.ai2.domain.BoardModel;
import com.hyunjin.ai2.persistence.BoardDAO;

@Service
public class BoardServiceImpl implements BoardService{

	@Inject
	private BoardDAO dao;
	
	@Override
	public List<BoardModel> list(BoardModel board)throws Exception{
		return dao.list(board);
	}
}
