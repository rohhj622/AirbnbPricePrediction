package com.hyunjin.ai2.controller;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.UUID;

import javax.inject.Inject;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.multipart.MultipartFile;

import com.hyunjin.ai2.domain.BoardModel;
import com.hyunjin.ai2.service.BoardService;


/**
 * Handles requests for the application home page.
 */
@Controller
public class DanHomeController {
	
	private static final Logger logger = LoggerFactory.getLogger(HomeController.class);
	
	/**
	 * Simply selects the home view to render by returning its name.
	 */

	@RequestMapping(value="/fileupload",method=RequestMethod.GET)
	public String fileuploadGET()throws Exception{
		return "fileupload";
	}
	@RequestMapping(value = "/fileupload",method = RequestMethod.POST)
	public void upload(MultipartFile uploadfile, Model model){
	    logger.info("upload() POST 호출");
	    logger.info("파일 이름: {}", uploadfile.getOriginalFilename());
	    logger.info("파일 크기: {}", uploadfile.getSize());

	    String Name = saveFile(uploadfile);
	    model.addAttribute("fileName", Name);
	    
	}
	private String saveFile(MultipartFile file){
	    // 파일 이름 변경
	    UUID uuid = UUID.randomUUID();
	    //String RealName = uuid + "_" + file.getOriginalFilename();
	    String RealName = file.getOriginalFilename();
	    String saveName = "uploadFile.csv";

	    logger.info("saveName: {}",saveName);

	    // 저장할 File 객체를 생성(껍데기 파일)ㄴ
	    String UPLOAD_PATH="/Users/hyunjin/Desktop";
	    File saveFile = new File(UPLOAD_PATH, saveName); // 저장할 폴더 이름, 저장할 파일 이름

	    try {
	        file.transferTo(saveFile); // 업로드 파일에 saveFile이라는 껍데기 입힘
	    } catch (IOException e) {
	        e.printStackTrace();
	        return null;
	    }
	    
	    return RealName;
	}
	
	@RequestMapping(value="/test2",method=RequestMethod.GET)
	public void test2GET()throws Exception{
	}
	
	@RequestMapping(value="/popup",method=RequestMethod.GET)
	public void popupGET()throws Exception{
	}
	
	@Inject
	private BoardService service;
	@RequestMapping(value="/Analysis",method=RequestMethod.GET)
	public void listGET(BoardModel board, Model model)throws Exception{
		model.addAttribute("list", service.list(board));
	}
	
	@RequestMapping(value="/Analysis",method=RequestMethod.POST)
	public String AnalysisPOST(BoardModel board, Model model)throws Exception{
		Python(model);
		model.addAttribute("list", service.list(board));
		return "Analysis";
	}
	private void Python(Model model)throws Exception{
		
		BufferedReader input =null;
	     
	    try {
	        long start, end;
	        String line;
	        String execPath ="python /Users/hyunjin/Documents/spring-ex/aiTest/src/main/webapp/WEB-INF/views/main.py";
	         
	        start = System.currentTimeMillis();
	         
	        Process p = Runtime.getRuntime().exec(execPath);
	        input =new BufferedReader(new InputStreamReader(p.getInputStream()));
	        
	        line = input.readLine();
	        logger.info(line);
	        while ((line = input.readLine()) !=null) {
	            logger.info("Result : " + line);
	        }
	 
	        end = System.currentTimeMillis();
	 
	        logger.info("Running Time : " + (end - start) / 1000f +"s.");
	        model.addAttribute("result", "true");
	         
	    }catch (IOException err) {
	        err.printStackTrace();
	    }finally {
	        if (input !=null) input.close();
	    }
	    
	}
}
