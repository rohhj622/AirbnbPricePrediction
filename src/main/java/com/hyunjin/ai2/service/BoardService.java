package com.hyunjin.ai2.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.hyunjin.ai2.domain.BoardModel;

public interface BoardService {

	public List<BoardModel> list(BoardModel board)throws Exception;
}
