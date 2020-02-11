package com.ads.usermanagement.UserManagement.controllers;

import com.ads.usermanagement.UserManagement.models.AuthenticationRequest;
import com.ads.usermanagement.UserManagement.models.AuthenticationResponse;
import com.ads.usermanagement.UserManagement.models.Users;
import com.ads.usermanagement.UserManagement.service.UserService;
import com.ads.usermanagement.UserManagement.util.JwtUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

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
    ResponseEntity<String> register(@RequestBody Users users) throws Exception
    {
        Users u = new Users();
        u.setName(users.getName());
        u.setUsername(users.getUsername());
        u.setRole(users.getRole());
        u.setPassword(passwordEncoder.encode(users.getPassword()));
        String s = userService.registerUsers(u);
        return new ResponseEntity<>(s, HttpStatus.OK);
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
        return ResponseEntity.ok(new AuthenticationResponse(jwt));

    }
}
