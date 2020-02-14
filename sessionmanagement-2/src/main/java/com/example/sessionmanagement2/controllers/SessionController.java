package com.example.sessionmanagement2.controllers;

import com.example.sessionmanagement2.models.SessionManagementData;
import com.example.sessionmanagement2.repository.SessionRepository;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SessionController {
    public SessionController(SessionRepository sessionRepository) {
        this.sessionRepository = sessionRepository;
    }

    private final SessionRepository sessionRepository;
    @PostMapping("/getSessionData")
    public String getSessionData(@RequestBody SessionManagementData sm)
    {

        System.out.println("SM is : " + sm);
        sessionRepository.save(sm);
        return "Hello";
    }
}
