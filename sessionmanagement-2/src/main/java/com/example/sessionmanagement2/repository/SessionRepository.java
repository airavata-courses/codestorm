package com.example.sessionmanagement2.repository;

import com.example.sessionmanagement2.models.SessionManagementData;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;
import org.springframework.data.repository.query.Param;
//import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import java.util.List;

@EnableMongoRepositories(basePackageClasses = SessionRepository.class)
@Configuration
public interface SessionRepository extends MongoRepository<SessionManagementData, Integer> {

    public List<SessionManagementData> findByUserName(@Param("userName")String userName);

}
