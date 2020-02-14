
import { API_BASE_URL, ACCESS_TOKEN } from '../constants';

const axios = require('axios');

const request = (options) => {
    const headers = new Headers({
        'Content-Type': 'application/json',
    })
    
    if(localStorage.getItem(ACCESS_TOKEN)) {
        headers.append('Authorization', 'Bearer ' + localStorage.getItem(ACCESS_TOKEN))
    }

    const defaults = {headers: headers};
    options = Object.assign({}, defaults, options);

    return fetch(options.url, options)
    .then(response => 
        response.json().then(json => {
            if(!response.ok) {
                return Promise.reject(json);
            }
            return json;
        })
    );
};

export function login(loginRequest) {
    console.log("InsideAPIUtils Login REQQUEEEESSTTT",loginRequest);
    return request({
        url: API_BASE_URL + "/authenticate",
        method: 'POST',
        body: JSON.stringify(loginRequest)
    });
}

export function signup(signupRequest) {
    console.log("signup")
    return request({
        url: API_BASE_URL + "/register",
        method: 'POST',
        body: JSON.stringify(signupRequest)
    });
}

export function getCurrentUser() {
    
    if(!localStorage.getItem(ACCESS_TOKEN)) {
        console.log("no access token")
        return Promise.reject("No access token set.");
    }

    console.log(localStorage.getItem(ACCESS_TOKEN))
    console.log("calling api gateway")

    return request({
        url: API_BASE_URL + "/user/me",
        method: 'GET'
    });
}

export function getWeatherData(req,res) {

    console.log("In getWeatherData")

    return axios({
        url: API_BASE_URL + "/getWeatherData",
        method: 'GET'
    })
    //.then(res => res.json())
    //    .then((data) => {
    //    console.log(response)
    //   weatherData.setState({weatherData : res.data })
    //    })
    //    .catch(console.log)
}

export function performAnalysis() {

    console.log("In performAnalysis")

    return request({
        url: API_BASE_URL + "/modelexecution",
        method: 'GET'
    });

}

export function getUserProfile(username) {
    return request({
        url: API_BASE_URL + "/users/" + username,
        method: 'GET'
    });
}

