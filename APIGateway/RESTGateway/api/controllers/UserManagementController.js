const axios = require('axios');
var utils = require('../utils');

exports.login = function(req, res) {

    console.log("Inside login")
    
    var host='localhost';
    var port='8085';
    
    var url = "http://"+host+":"+port.toString()+"/authenticate";
    var username, password;
    username = req.body.usernameOrEmai;
    password = req.body.password;

    return axios({
        method: "post",
        url:"http://localhost:8085/authenticate",
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

        utils.addNewSession({
            requestTime:new Date(),
            userName: username,
            requestName: "Login",
            requestStatus:true
          });

        })
        .catch(err => {
        console.log(err);
        res.send({ err });
        });
};

exports.register = function(req, res) {

    console.log("Inside register")

    name = req.body.name;
    username = req.body.username;
    role = req.body.role;
    password = req.body.password;

    return axios({
        method: "post",
        url:"http://localhost:8085/register",
        headers: {
            "Access-Control-Allow-Origin": "*"
        },
        data: {
            "name": name,
            "username": username,
            "role": role,
            "password": password
        }
        })
        .then(response => {
        console.log("Response:"+response.data);
        res.send(response.data);
        })
        .catch(err => {
        console.log("Error"+err);
        res.send({ err });
        });

};

exports.loadcurrentuser = function(req, res) {

    console.log("Inside Load Current user")
    console.log(req.headers.authorization)
    var host='localhost';
    var port='8085';
    
    var url = "http://"+host+":"+port.toString()+"/user/me";
    console.log("*******************************",req.headers.authorization);
    return axios({
        
        method: "get",
        url:"http://localhost:8085/user/me",
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Authorization": req.headers.authorization
        }
        })
        .then(response => {
        console.log("Response:"+response.data);
        res.send(response.data);
        })
        .catch(err => {
        console.log("Error"+err);
        res.send({ err });
        });
    
};


