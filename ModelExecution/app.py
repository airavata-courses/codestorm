# importing reuired libraries
from flask import Flask
from flask_cors import CORS,cross_origin
# from netCDF4 import Dataset
# import generate_plot as gp
import model_data_consumer as mdc
import model_res as mr
import model_data_res_producer as mdp
import jsonpickle
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import pandas as pd
import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.plots import Hodograph, SkewT
from metpy.units import units

import matplotlib
matplotlib.use('Agg')
# from matplotlib.pyplot import subplots


# initializing flask application
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

# enabling cross origin access to any source
# Once the applciation is deployed, the '*' will be replaced with
# source URL
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/modelexecution")
def helper():
    print("Inside def helper")
    df = mdc.md_consumer()
    if(df is None):
        return "Please retrieve data first!"
    print(df, "value of df!!!!!!!!!!!!!!")
    if(df.empty):
        print("File object Empty!!!")
    else:
        print("File Object recieved!!",df)
    
    p = df['pressure'].values * units.hPa
    T = df['temperature'].values * units.degC
    Td = df['dewpoint'].values * units.degC
    wind_speed = df['speed'].values * units.knots
    wind_dir = df['direction'].values * units.degrees
    u, v = mpcalc.wind_components(wind_speed, wind_dir)
    response = "Model Execution is done."

    make_plot(p,T,Td,u,v)



 




    return jsonpickle.encode(response, unpicklable=False), 200
    


def make_plot(p,T,Td,u,v):

       # Calculate the LCL
    lcl_pressure, lcl_temperature = mpcalc.lcl(p[0], T[0], Td[0])

    print(lcl_pressure, lcl_temperature)

# Calculate the parcel profile.
    parcel_prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')

# Create a new figure. The dimensions here give a good aspect ratio
    fig = plt.figure(figsize=(9, 9))
    skew = SkewT(fig)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
    skew.plot(p, T, 'r', linewidth=2)
    skew.plot(p, Td, 'g', linewidth=2)
    skew.plot_barbs(p, u, v)

    # fig=plt.save()

    # # use the subplots function to create a single plot
    # # this makes things easier as you move to multipanel plotting
    # fig, ax = subplots()

    # # use the plot method of the axis object
    # ax.plot(temp)

    # # # optional commands

    # # # add gridlines to the plot
    # ax.grid()

    # # # set limits for the x axis, 1440 total time values
    # ax.set_xlim(0,1439)

    # # # add a title
    # ax.set_title('Mean Temperature')

    # # # use the savefig function attached to the figure object, saving the figure
    fig.savefig('lineplot.png', dpi=300)
    image_link = mr.helper()
    s = mdp.md_producer(image_link)

    print("Imaaagggeeeee Linkkkkkkkk", image_link)
    return s

# # Starting the application server
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 7500)
