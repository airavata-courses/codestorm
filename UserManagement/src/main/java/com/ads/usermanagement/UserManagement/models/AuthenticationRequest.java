package com.ads.usermanagement.UserManagement.models;//package com.io.mongo_connections.MongoConnections.models;

import com.ads.usermanagement.UserManagement.repository.UserRepository;


import java.io.Serializable;

public class AuthenticationRequest implements Serializable {

    UserRepository userRepository;

    private String username;
    private String password;

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    //need default constructor for JSON Parsing
    public AuthenticationRequest()
    {

    }

    public AuthenticationRequest(String username, String password) {
        this.setUsername(username);
        this.setPassword(password);
    }
}
