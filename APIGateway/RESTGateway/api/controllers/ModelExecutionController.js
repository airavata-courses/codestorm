const axios = require('axios')

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
          })
          .catch(err => {
            console.log(err);
          });
    
};