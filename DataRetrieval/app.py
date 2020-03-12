from flask import Flask
from flask_cors import CORS,cross_origin
import jsonpickle
import data_retrieval_producer as drp
# import matplotlib.pyplot as plt
# from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import pandas as pd
import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.plots import Hodograph, SkewT
from metpy.units import units
import matplotlib as matplotlib
matplotlib.use('Agg')


# initializing flask application
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

# enabling cross origin access to any source
# Once the applciation is deployed, the '*' will be replaced with
# source URL
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/getWeatherData")
def retrieve_data():

    col_names = ['pressure', 'height', 'temperature', 'dewpoint', 'direction', 'speed']

    df = pd.read_fwf(get_test_data('nov11_sounding.txt', as_file_obj=False),
                 skiprows=5, usecols=[0, 1, 2, 3, 6, 7], names=col_names)

# Drop any rows with all NaN values for T, Td, winds
    df = df.dropna(subset=('temperature', 'dewpoint', 'direction', 'speed'
                       ), how='all').reset_index(drop=True)




# We will pull the data out of the example dataset into individual variables and
# assign units.

    # p = df['pressure'].values * units.hPa
    # T = df['temperature'].values * units.degC
    # Td = df['dewpoint'].values * units.degC
    # wind_speed = df['speed'].values * units.knots
    # wind_dir = df['direction'].values * units.degrees
    # u, v = mpcalc.wind_components(wind_speed, wind_dir)






# # Calculate the LCL
#     lcl_pressure, lcl_temperature = mpcalc.lcl(p[0], T[0], Td[0])

#     print(lcl_pressure, lcl_temperature)

# # Calculate the parcel profile.
#     parcel_prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')

# # Create a new figure. The dimensions here give a good aspect ratio
#     fig = plt.figure(figsize=(9, 9))
#     skew = SkewT(fig)

# # Plot the data using normal plotting functions, in this case using
# # log scaling in Y, as dictated by the typical meteorological plot
#     skew.plot(p, T, 'r', linewidth=2)
#     skew.plot(p, Td, 'g', linewidth=2)
#     skew.plot_barbs(p, u, v)

    
    status= drp.dr_producer(df)
    print("Successfully Produced!",status)
    response = "The dataframe data is \n" + str(df) 
    return jsonpickle.encode(response, unpicklable=False), 200
#     return "Hello World!!!"
 
# Show the plot
   # plt.save()

# # importing reuired libraries
# from flask import Flask
# from flask_cors import CORS,cross_origin
# from netCDF4 import Dataset
# import jsonpickle
# import matplotlib

# from matplotlib.pyplot import subplots
# import data_retrieval_producer as drp


# # initializing flask application
# app = Flask(__name__, static_url_path='/static')
# app.config.from_object(__name__)

# # enabling cross origin access to any source
# # Once the applciation is deployed, the '*' will be replaced with
# # source URL
# app.config['CORS_HEADERS'] = 'Content-Type'
# cors = CORS(app, resources={r"/*": {"origins": "*"}})


# @app.route("/getWeatherData")
# def retrieve_data():
#     # Path to netCDF file, change /data_path/ to match where the file is located on your system
#     file_name = 'sgpmetE13.b1.20140218.000000.cdf'

#     # use the Dataset function to create an object reference to the open netCDF file
#     file_obj = Dataset(file_name)

#     # printing the file object displays the python type, global attributes, file dimensions,
#     # and variables in the file
#     print(file_obj)

#     # print only the global attributes
#     print(file_obj.ncattrs())

#     # print only the global attributes
#     print(file_obj.ncattrs())


#     # method 2 this is actually preferable if you need to loop over multiple attribute names
#     #    because you can use a string as the key for the attribute name
#     print(file_obj.getncattr('history'))


#     # print list of file dimension names to the screen ('u' simply means unicode string)
#     print(file_obj.dimensions.keys())

#     # print list of variable names to screen ('u' simply means unicode string)
#     print(file_obj.variables.keys())

#     # load information from temperature variable into object
#     temp_obj = file_obj.variables['temp_mean']

#     # print information about the temperature variable
#     print(temp_obj)

#     # print variable attributes for temp_mean variable ('u' simply means unicode string)
#     print(temp_obj.ncattrs())

#     # access a variable attribute:

#     # method 1
#     print(temp_obj.long_name)


#     # method 2 - this is actually preferable if you need to loop over multiple attribute names
#     #    because you can use a string as the key for the attribute name
#     print(temp_obj.getncattr('long_name'))

#     print(temp_obj[:])
#     temp = temp_obj[:]

#     drp.dr_producer(temp)
#     response = "The temperature data is \n" + str(temp_obj) 
#     #return jsonpickle.encode(response, unpicklable=False), 200
#     return "Hello World!!!"

if __name__ == '__main__':
 	app.run(host = '0.0.0.0', port = 7000)

