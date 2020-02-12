package com.ads.usermanagement.UserManagement;

import com.ads.usermanagement.UserManagement.models.Users;
import com.ads.usermanagement.UserManagement.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class UserManagementApplication implements CommandLineRunner {

	private UserRepository userRepository;

	@Autowired
	public UserManagementApplication(UserRepository userRepository)
	{
		this.userRepository = userRepository;
	}

	public static void main(String[] args) {
		SpringApplication.run(UserManagementApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
	}

}
