const axios = require('axios')
var utils = require('../utils');

exports.getWeatherData = function(req,res) {
    console.log("Inside getWeatherData");
    var host='localhost';
    var port ='7000';
     
    
        return axios({
            method: "get",
            //url: "http://dataretrieval:7000/getWeatherData",
            url: "http://149.165.170.97:30007/getWeatherData",
            headers: {
              "Access-Control-Allow-Origin": "*"
            }
          })
          .then(response => {
            console.log("Recieved response inside DRC then response")
            res.send(response.data);
            utils.addNewSession({
              requestTime:new Date(),
              requestName: "Data Retrieval",
              requestStatus:true
            });
          })
          .catch(err => {
            console.log(err);
          });
    
};
