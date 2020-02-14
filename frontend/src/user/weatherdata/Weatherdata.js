import React, { Component } from 'react';
import './Weatherdata.css';
import { Button } from 'antd';
//import { performAnalysis } from '../../util/APIUtils';
const axios = require('axios');
class Weatherdata extends Component {

    constructor(props) {
        super(props);
        this.state = {
          weatherData: ""     
        };  
        
    }
    
    getData(){
        return axios({
            method: "post",
            url:"http://localhost:4000/getWeatherData",
            headers: {
                "Access-Control-Allow-Origin": "*"
            }
            })
            .then(response => {
            console.log(response.data);
            alert(response.data)
            //this.setState({weatherData:response.data});
            //res.send(response.data);

            
            console.log("RESPONSE BY AUTHENTICATE!!!!!!!!!!!!!!!!!!!",response.data);
            // utils.addNewSession({
            //     requestTime:new Date(),
            //     userName: 'sia@iu.edu',
            //     requestName: "Login",
            //     requestStatus:true
            //   });
            })
            .catch(err => {
                alert("error")
            console.log(err);
            });
    }




    getAnalysis(){
        return axios({
            method: "get",
            url:"http://localhost:4000/modelexecution",
            headers: {
                "Access-Control-Allow-Origin": "*"
            }
            })
            .then(response => {
            console.log(response.data);
            alert(response.data)
            //this.setState({weatherData:response.data});
            //res.send(response.data);

            
            
            // utils.addNewSession({
            //     requestTime:new Date(),
            //     userName: 'sia@iu.edu',
            //     requestName: "Login",
            //     requestStatus:true
            //   });
            })
            .catch(err => {
                alert("error")
            console.log(err);
            });
    }



    getResults(){
        return axios({
            method: "get",
            url:"http://localhost:4000/postprocessing",
            headers: {
                "Access-Control-Allow-Origin": "*"
            }
            })
            .then(response => {
            console.log(response.data);
            alert("Click on the following Link:" , response.data)
            //this.setState({weatherData:response.data});
            //res.send(response.data);

            
            console.log("RESPONSE BY AUTHENTICATE!!!!!!!!!!!!!!!!!!!",response.data);
            // utils.addNewSession({
            //     requestTime:new Date(),
            //     userName: 'sia@iu.edu',
            //     requestName: "Login",
            //     requestStatus:true
            //   });
            })
            .catch(err => {
                alert("error")
            console.log(err);
            });
    }


    render() {
        return (
            <div className="weather-data">
                <h5>Process Weather Data</h5>
                <Button onClick={this.getData} className="go-back-btn" type="primary" size="large">Retrieve Data</Button>
                <br></br>
                <br></br>
                <label>
                 DataSatistics
                
                </label>
                <br></br>
                <br></br>
                <Button onClick={this.getAnalysis} className="go-back-btn" type="primary" size="large">Perform Analysis</Button>
                <br></br>
                <br></br>
                <Button onClick={this.getResults} className="go-back-btn" type="primary" size="large">Display Results</Button>
            </div>
        );
    }
}

export default Weatherdata;