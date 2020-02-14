const axios = require('axios');
var utils = require('../utils');

exports.getWeatherData = function(req, res) {
    console.log("Inside getWeatherData");
    var host='localhost';
    var port ='7000';
     
    
        return axios({
            method: "get",
            url: "http://localhost:7000/getWeatherData",
            headers: {
              "Access-Control-Allow-Origin": "*"
            }
          })
          .then(response => {
            console.log("Recieved response")
            console.log("inside response", response.data);
            res.send(response.data);
            // utils.addNewSession({
            //   requestTime:new Date(),
            //   userName: 'sia@iu.edu',
            //   requestName: "Data Retrieval",
            //   requestStatus:true
            // });
          })
          .catch(err => {
            console.log(err);
          });
    
};