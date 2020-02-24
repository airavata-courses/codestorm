const axios = require('axios')
var utils = require('../utils');

exports.postprocessing = function(req,res) {
    console.log("Inside postprocessing");
    var host='localhost';
    var port ='5500';

        return axios({
            method: "get",
            url: "http://localhost:5500/postprocessing",
            headers: {
              "Access-Control-Allow-Origin": "*"
            }
          })
          .then(response => {
            console.log("Recieved response")
            res.send(response.data);
            utils.addNewSession({
              requestTime:new Date(),
              requestName: "Post Processing",
              requestStatus:true
            });
          })
          .catch(err => {
            console.log(err);
          });
    
};