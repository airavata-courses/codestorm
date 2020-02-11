const axios = require('axios')

exports.getWeatherData = function(url,req.body.token,response) {
    var host='localhost';
    var port ='7000';
     
    
        return axios({
            method: "post",
            url: "http://"+host+":"+port.toString()+'/getWeatherData',
            headers: {
              "Access-Control-Allow-Origin": "*"
            }
          })
          .then(response => {
            console.log("Recieved response")
          })
          .catch(err => {
            console.log(err);
          });
    
};