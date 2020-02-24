'use strict';
var jwt = require('jsonwebtoken');
const axios = require('axios');

module.exports = {
  getAuthToken: function (req) {
      auth_header = req.header('Authorization');
      if (auth_header && auth_header.split(' ')[0] === 'Bearer') {
          return auth_header.split(' ')[1];
      } else {
          return null;
      }
  }
}

module.exports = {
    addNewSession: function(sessionToSave) {
    var host,port,url;

    var path = '/session_management';
    console.log("Inside utils.js")
    console.log(sessionToSave);   
        
        return axios({
            method: "post",
            url: "http://localhost:8089/getSessionData",
            headers: {
              "Access-Control-Allow-Origin": "*"
            },
            data: sessionToSave
          })
          .then(response => {
            console.log("Response received from SM springboot!!!!!!")
            console.log(response.data);
            return response.data;
            
          })
          .catch(err => {
            console.log(err);
            return err.data;
          });
    }
}