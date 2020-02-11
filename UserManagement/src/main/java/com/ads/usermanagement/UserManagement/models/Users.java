package com.ads.usermanagement.UserManagement.models;

import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.MongoId;

    @Document(collection = "user")
    public class Users {

        @MongoId
        private String id;
        private String name;
        private String username;
        private String password;
        private String role;

        public Users() {
        }

        public Users(String name, String username, String password, String role) {
            this.name = name;
            this.username = username;
            this.password = password;
            this.role = role;
        }

        public String get_id()
        {
            return id;
        }

        public void set_id(String id)
        {
            this.id = id;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

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

        public String getRole() {
            return role;
        }

        public void setRole(String role) {
            this.role = role;
        }

        public String toString()
        {
            return String.format("User[id = '%s', name = '%s', username = '%s', password = '%s', role = '%s']", id, name, username, password, role);
        }
    }

