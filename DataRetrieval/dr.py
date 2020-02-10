# -*- coding: utf-8 -*-

# !pip install netCDF4

# !wget https://noaa-nexrad-level2.s3.amazonaws.com/1991/07/05/KTLX/KTLX19910705_235109.gz

# !pip install arm_pyart

#!gunzip /content/KTLX19910705_235109.gz

print(__doc__)

# Author: Jonathan J. Helmus (jhelmus@anl.gov)
# License: BSD 3 clause

import matplotlib.pyplot as plt
import pyart
import netCDF4
from flask import Flask
from flask_cors import CORS
from flask_script import Manager
from confluent_kafka import Producer


app=Flask(__name__)

manager = Manager(app)

CORS(app, support_credentials=True)

@app.route("/")
def retrieve_data():
    # read the data and create the display object
    filename = 'KTLX19910705_235109'
    radar = pyart.io.read_nexrad_archive(filename)
    display = pyart.graph.RadarDisplay(radar)

    # fields to plot and ranges
    fields_to_plot = ['reflectivity', 'velocity']
    ranges = [(-32, 64), (-17.0, 17.0)]

    # # plot the data
    nplots = len(fields_to_plot)
    plt.figure(figsize=[5 * nplots, 4])

    serialize_weather_data = pickle.dumps(weather_data)
    # plot each field
    for plot_num in range(nplots):
      field = fields_to_plot[plot_num]
      plt.subplot(1, nplots, plot_num + 1)
      weather_data_plot =display.plot(field, 0, vmin=vmin, vmax=vmax, title_flag=False)
      display.set_limits(ylim=[0, 17])

     # set the figure title and show
    # instrument_name = radar.metadata['instrument_name']
    # time_start = netCDF4.num2date(radar.time['data'][0], radar.time['units'])
    # time_text = ' ' + time_start.isoformat() + 'Z '
    # azimuth = radar.fixed_angle['data'][0]
    # title = 'RHI ' + instrument_name + time_text + 'Azimuth %.2f' % (azimuth)
    # plt.suptitle(title)
    # plt.show()

    serialize_weather_data = pickle.dumps(weather_data_plot)
    
    return serialize_weather_data

def delivery_report(err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


def confluent_kafka_produce():
    p = Producer({'bootstrap.servers': 'localhost:9092'})
    weather_data=retrieve_data()
    weather_data_source=weather_data#["hello","world""hello","world","hello","world","hello","world","hello","world"]
    for data in weather_data_sorce:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)
    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    serialize_weather_data = pickle.dumps(data)
    p.produce('Hello_World', data.encode('utf-8'), callback=delivery_report)

    # Wait for any outstanding messages to be delivered and delivery report
    # callbacks to be triggered.
    p.flush()

if __name__ == "__main__":
    #registerFetchWeatherDataService('127.10.10.7', 3000)
    app.run(host='127.10.10.7', port=4000)


