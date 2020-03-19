package com.ads.usermanagement.UserManagement.controllers;
import com.ads.usermanagement.UserManagement.models.AuthenticationRequest;
import com.ads.usermanagement.UserManagement.models.AuthenticationResponse;
import com.ads.usermanagement.UserManagement.models.Users;
import com.ads.usermanagement.UserManagement.payload.UserSummary;
import com.ads.usermanagement.UserManagement.security.CurrentUser;
import com.ads.usermanagement.UserManagement.security.UserPrincipal;
import com.ads.usermanagement.UserManagement.service.UserService;
import com.ads.usermanagement.UserManagement.util.JwtUtil;

import java.net.URI;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

@RestController
public class UserResource {

    Logger logger = LoggerFactory.getLogger(UserResource.class);

    @Autowired
    private AuthenticationManager authenticationManager;

    @Autowired
    private UserService userService;

    @Autowired
    private JwtUtil jwtTokenUtil;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @GetMapping("/hello")
    public String hello()
    {
        return ("Hello World!!!");
    }

    @CrossOrigin(origins = "*")
    @RequestMapping(value = "/register", method = RequestMethod.POST)
    ResponseEntity<?> register(@RequestBody Users users) throws Exception
    {
        Users u = new Users();
        u.setName(users.getName());
        u.setUsername(users.getUsername());
        u.setRole(users.getRole());
        u.setPassword(passwordEncoder.encode(users.getPassword()));
        String s = userService.registerUsers(u);
        
        if(s.length() > 0) {
        	
        	URI location = ServletUriComponentsBuilder
                    .fromCurrentContextPath().path("/users/{username}")
                    .buildAndExpand(u.getUsername()).toUri();
        	
        	return ResponseEntity.created(location).body(new AuthenticationResponse(true, "User is registered successfully!"));
        	
        } else {
        	
        	return new ResponseEntity(new AuthenticationResponse(false, "Username is already taken!"),
                    HttpStatus.BAD_REQUEST);
        	
        }
        
    }

    @CrossOrigin(origins = "*")
    @RequestMapping(value = "/authenticate", method = RequestMethod.POST)
    public ResponseEntity<?> createAuthenticationToken(@RequestBody AuthenticationRequest authenticationRequest) throws Exception {

        try {
            // verify whether pwd is matching.
            authenticationManager.authenticate(
                    new UsernamePasswordAuthenticationToken(authenticationRequest.getUsername(), authenticationRequest.getPassword())
            );
        } catch (BadCredentialsException e) {
            logger.error("Incorrect username or password" + e);
        }

        final UserDetails userDetails = userService.loadUserByUsername(authenticationRequest.getUsername());
        final String jwt = jwtTokenUtil.generateToken(userDetails);
        logger.trace("JWT TOKEN is : " + jwt);

        //Everything is OK. Payload of Response Entity will have AuthenticationResponse(jwt).
        //AuthenticationResponse(jwt) is the class in model.
        System.out.println(jwt);
        System.out.println(ResponseEntity.ok(new AuthenticationResponse(jwt)));
        return ResponseEntity.ok(new AuthenticationResponse(jwt));

    }
    
    @GetMapping("/user/me")
    public UserSummary getCurrentUser(@CurrentUser UserDetails currentUser) {
    	System.out.println(currentUser);
        UserSummary userSummary = new UserSummary(currentUser.getUsername());
        System.out.println(userSummary);
        return userSummary;
    }
    
}
