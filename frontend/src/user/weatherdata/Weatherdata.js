import React, { Component } from 'react';
import './Weatherdata.css';
import { Button } from 'antd';
import { getWeatherData, performAnalysis } from '../../util/APIUtils';

class Weatherdata extends Component {

    render() {
        return (
            <div className="weather-data">
                <h5>Process Weather Data</h5>
                <Button onClick={getWeatherData} className="go-back-btn" type="primary" size="large">Retrieve Data</Button>
                <br></br>
                <br></br>
                <Button onClick={performAnalysis} className="go-back-btn" type="primary" size="large">Perform Analysis</Button>
            </div>
        );
    }
}

export default Weatherdata;