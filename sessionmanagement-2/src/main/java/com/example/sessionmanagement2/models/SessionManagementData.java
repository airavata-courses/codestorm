package com.example.sessionmanagement2.models;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.MongoId;

@Document(collection = "sessiondata")
public class SessionManagementData {

    @Id
    @MongoId
//    @GeneratedValue(strategy = GenerationType.AUTO)
    private String id;
    private String userName;
    private String requestName;
    private String requestTime;
    private String requestStatus;

    public SessionManagementData() {
    }

    public SessionManagementData(String requestTime, String username, String reqName, String requestStatus)
    {
        this.userName = username;
        this.requestName = reqName;
        this.requestTime = requestTime;
        this.requestStatus = requestStatus;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getRequestName() {
        return requestName;
    }

    public void setRequestName(String requestName) {
        this.requestName = requestName;
    }

    public String getRequestTime() {
        return requestTime;
    }

    public void setRequestTime(String requestTime) {
        this.requestTime = requestTime;
    }

    public String getRequestStatus() {
        return requestStatus;
    }

    public void setRequeststatus(String requeststatus) {
        this.requestStatus = requeststatus;
    }



    public String toString()
    {
        return String.format("User[username = '%s', requestName = '%s', requestTime = '%s', requestStatus = '%s']", userName, requestName, requestTime, requestStatus);
    }

}
