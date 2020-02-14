const axios = require('axios')
var utils = require('../utils');

exports.getModelExecutionStatus = function(req,res) {
    console.log("Inside getModelExecutionStatus");
      return axios({
            method: "get",
            url: "http://localhost:7500/modelexecution",
            headers: {
              "Access-Control-Allow-Origin": "*"
            }
          })
          .then(response => {
            console.log("Recieved response")
            res.send(response.data);
            // utils.addNewSession({
            //   requestTime:new Date(),
            //   userName: 'sia@iu.edu',
            //   requestName: "Model Execution",
            //   requestStatus:true
            // });
          })
          .catch(err => {
            console.log(err);
          });   
};
// response is the response of modelexecution api