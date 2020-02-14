const axios = require('axios');
const util = require('../utils');    
  exports.sendsessiondata= function(req,res) {
    console.log("Inside Session Management Controller !!!!!!!!!!!!!!!!!!!!!")
        return axios({
            method: "post",
            url: "http://localhost:8089/getSessionData",
            headers: {
              "Access-Control-Allow-Origin": "*"
            }
          })
          .then(response => {
            res.send(response.data);
          })
          .catch(err => {
            res.send(err.response.status).send(err.response.body);
          });
};  