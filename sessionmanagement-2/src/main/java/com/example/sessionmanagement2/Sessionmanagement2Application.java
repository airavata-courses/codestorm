package com.example.sessionmanagement2;

import com.example.sessionmanagement2.models.SessionManagementData;
import com.example.sessionmanagement2.repository.SessionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@SpringBootApplication
public class Sessionmanagement2Application {

//	@Autowired
//	private SessionRepository repository;


//	@RequestMapping(value = "/getSessionData", method = RequestMethod.POST)
//	public String getSessionData(@RequestBody SessionManagementData sm)
//	{
//		System.out.println("Inside SessionManagementData!!!!!!!!!!!!!!!!!!");

//		if(sm == null)
//			System.out.println("sm is null!!!!!!!!!!!");
//		repository.save(sm);
//		String s = "Session for username " + sm.getUsername() + " saved successfully!!!";
//
//		System.out.println("From Hello of SM and smd is : " + sm);
//		System.out.println(s);
//		return "Got it!!!!!!";
//	}

	public static void main(String[] args) {
		SpringApplication.run(Sessionmanagement2Application.class, args);
	}

}
