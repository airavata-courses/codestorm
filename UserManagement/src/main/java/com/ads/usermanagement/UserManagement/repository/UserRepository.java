package com.ads.usermanagement.UserManagement.repository;

import com.ads.usermanagement.UserManagement.models.Users;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;
import org.springframework.data.repository.query.Param;

@EnableMongoRepositories(basePackageClasses = UserRepository.class)
@Configuration
public interface UserRepository extends MongoRepository<Users, String>
{
    public Users findByUsername(@Param("username")String username);
}

