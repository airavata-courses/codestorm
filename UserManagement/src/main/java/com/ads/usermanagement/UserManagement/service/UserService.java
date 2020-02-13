package com.ads.usermanagement.UserManagement.service;

import com.ads.usermanagement.UserManagement.models.Users;
import com.ads.usermanagement.UserManagement.repository.UserRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.ArrayList;

@Service
public class UserService implements UserDetailsService{

    Logger logger = LoggerFactory.getLogger(UserService.class);

    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String s) throws UsernameNotFoundException, DataAccessException {

        Users user = userRepository.findByUsername(s);

        if (user == null)
        {
            logger.error("User " + s + " not found");
            throw new UsernameNotFoundException("User not found!");
        }

        logger.trace("User found : "+ user.getUsername());

        return new User(user.getUsername(), user.getPassword(), true, true, true, true, new ArrayList<>());
    }

    public String registerUsers(Users user)
    {
        String s;
        // checking whether user is already registered.
        Users u = null;
        u = userRepository.findByUsername(user.getUsername());

        if(u == null)
        {
            userRepository.save(user);
            s = " User " + user.getName() + " with username : " + user.getUsername() + " successfully registered!";
        }
        else
            // s = "Registration failed, User with username " + user.getUsername() + " already exists. ";
        	s = "";
        return s;
    }
}
