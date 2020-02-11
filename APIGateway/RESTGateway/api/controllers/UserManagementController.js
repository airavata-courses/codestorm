const axios = require('axios');
//var utils = require('../utils');

exports.login = function(req, res) {

    console.log("Inside login")
    
    var host='localhost';
    var port='8081';
    
    var url = "http://"+host+":"+port.toString()+"/authenticate";
    var username, password;
    username = req.body.username;
    password = req.body.password;
    return axios({
        method: "post",
        url:"http://localhost:8081/authenticate",
        headers: {
            "Access-Control-Allow-Origin": "*"
        },
        data: {
            "username": username,
            "password": password
        }
        })
        .then(response => {
        console.log(response.data);
        res.send(response.data);
        })
        .catch(err => {
        console.log(err);
        res.send({ err });
        });
    
};

// exports.register = function(req, res) {
//     var zookeeper = require('node-zookeeper-client');
//     var host,port;
//     var client = zookeeper.createClient('localhost:2181');
//     var path = '/user_management';
//     var url;
//     var username, password;
    
//     client.getData(
//         path,
//         function (event) {
//             console.log('Got event: %s.', event);
//         },
//         function (error, data, stat) {
//             if (error) {
//                 console.log(error.stack);
//                 return;
//             }
//             zookeeper_data = JSON.parse(data.toString('utf8'))
//             host = zookeeper_data["host"];
//             port = zookeeper_data["port"];
//             console.log(host);
//             console.log(port);
            
//             url = "http://" + host + ":" + port.toString() + '/auth/register';
//             console.log(url);

//             username = req.body.username;
//             email = req.body.email;
//             password = req.body.password;

//             console.log(username + ', ' + email + ', ' + password);
//             RegisterAPICall(url, username, email, password, res);
//         }
//     );    
    
//     client.connect();

//     function RegisterAPICall(url, username, email, password, res)
//     {
//         return axios({
//             method: "post",
//             url: url,
//             headers: {
//               "Access-Control-Allow-Origin": "*"
//             },
//             data: {
//                 "username": username,
//                 "email": email,
//                 "password": password
//             }
//           })
//           .then(response => {
//             console.log(response.data);
//             util.addNewSession({
//                 requestTime:new Date(),
//                 userName: username,
//                 requestName: "Register",
//                 requestStatus:true
//             });
//             res.send(response.data);
//           })
//           .catch(err => {
//             console.log(err);
//             res.send({ err });
//           });
//     }
// };

// exports.user_details = function(req, res) {
//     var zookeeper = require('node-zookeeper-client');
//     var host,port;
//     var path = '/user_management';
//     var url='';
//     var username, password;

//     return axios({
//         method: "get",
//         url: url,
//         headers: {
//         "Access-Control-Allow-Origin": "*",
//         "Authorization": "Bearer " + token
//         }
//         })
//         .then(response => {
//         console.log(response.data);
//         res.send(response.data);
//         })
//         .catch(err => {
//             console.log(err);
//             res.send({ err });
//           });
       
    
// };