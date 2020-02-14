package com.ads.usermanagement.UserManagement.models;

import java.io.Serializable;

public class AuthenticationResponse implements Serializable{

    private final String jwt;
    private Boolean success;
    private String message;

    public AuthenticationResponse(String jwt) {
        this.jwt = jwt;
    }

    public String getJwt() {
        return jwt;
    }
    
    public AuthenticationResponse(Boolean success, String message) {
        this.jwt = "";
		this.success = success;
        this.message = message;
    }
    
}
