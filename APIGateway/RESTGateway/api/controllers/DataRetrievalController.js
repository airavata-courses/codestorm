const axios = require('axios')

exports.getWeatherData = function(req,res) {
    console.log("Inside getWeatherData");
    var host='localhost';
    var port ='7000';
     
    
        return axios({
            method: "get",
            url: "http://localhost:5000/getWeatherData",
            headers: {
              "Access-Control-Allow-Origin": "*"
            }
          })
          .then(response => {
            console.log("Recieved response")
            res.send(response.data);
          })
          .catch(err => {
            console.log(err);
          });
    
};