package com.hyunjin.ai2.controller;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.UUID;

import javax.inject.Inject;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;

import com.hyunjin.ai2.domain.AirbnbResultVO;
import com.hyunjin.ai2.service.AirbnbResultService;

/**
 * Handles requests for the application home page.
 */
@Controller
public class FileUploadController{
	
	@Inject
	AirbnbResultService service;
	
	private static final Logger logger = LoggerFactory.getLogger(FileUploadController.class);
	
	/**
	 * Simply selects the home view to render by returning its name.
	 * @throws Exception 
	 */
	@RequestMapping(value = "/fileupload")
	public String upload(MultipartFile uploadfile,@RequestParam("country")String country,Model model) throws Exception{
	    
	
		
		logger.info(country);
		// 파일 이름 변경
	    UUID uuid = UUID.randomUUID();
	    
	    // 저장시, 파일 이름
	    String saveName = uuid + "_" + uploadfile.getOriginalFilename();
	    
	    
	    logger.info("upload() POST 호출");
	    logger.info("파일 이름: {}", uploadfile.getOriginalFilename());
	    logger.info("파일 크기: {}", uploadfile.getSize());
	    
	    // 파일 저장	    
        saveFile(uploadfile,saveName);
        
        // 파이선 파일 실행
        callPython(saveName,country);
	    
       
        List<AirbnbResultVO> resultList=service.selectResult();
        
        model.addAttribute("resultList", resultList);
        
	    return "test";

	}
	
	
	// 파일 업로드
	private void saveFile(MultipartFile file, String saveName){

	    logger.info("saveName: {}",saveName);

	    // 저장할 File 객체를 생성(껍데기 파일)ㄴ
	    File saveFile = new File("/Users/hyunjin/Desktop",saveName); // 저장할 폴더 이름, 저장할 파일 이름

	    try {
	        file.transferTo(saveFile); // 업로드 파일에 saveFile이라는 껍데기 입힘
	    } catch (IOException e) {
	        e.printStackTrace();
	   
	    }

	} // end saveFile
	
	private void callPython(String saveName,String country) throws IOException {
		BufferedReader input =null;
	     
	    try {
	        long start, end;
	        String line;
	        String execPath ="python //Users/hyunjin/Documents/spring-ex/aiTest/src/main/webapp/WEB-INF/views/DataCleaning7.py"+
	        				" "+saveName+" "+country;
	        
	        logger.info("execPath : " + execPath);
	        start = System.currentTimeMillis();
	         
	        Process p = Runtime.getRuntime().exec(execPath);
	        input = new BufferedReader(new InputStreamReader(p.getInputStream()));
	 
	        while ((line = input.readLine()) !=null) {
	            logger.info("Result : " + line);
	        }
	 
	        end = System.currentTimeMillis();
	 
	        logger.info(""
	        		+ "Running Time : " + (end - start) / 1000f +"s.");
	         
	    }catch (IOException err) {
	        err.printStackTrace();
	    }finally {
	        if (input !=null) input.close();
	    }
	    
	}

	
}
