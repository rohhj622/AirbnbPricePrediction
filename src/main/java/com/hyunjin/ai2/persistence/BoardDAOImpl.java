package com.hyunjin.ai2.persistence;

import java.util.List;

import javax.inject.Inject;

import org.apache.ibatis.session.SqlSession;
import org.springframework.stereotype.Repository;

import com.hyunjin.ai2.domain.BoardModel;

@Repository
public class BoardDAOImpl implements BoardDAO{

	@Inject
	private SqlSession session;
	
	private static String namespace="com.hyunjin.mappers.AIMapper";
	
	@Override
	public List<BoardModel> list(BoardModel board)throws Exception{
		return session.selectList(namespace+".list",board);
	}
}
