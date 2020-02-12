#from matplotlib.pyplot import subplots
# importing reuired libraries
from flask import Flask
from flask_cors import CORS,cross_origin
from netCDF4 import Dataset
#import generate_plot as gp
# must insert this statement to render the plots within the notebook
# this is specific to the ipython notebook
#%matplotlib inline
# import subplots function for plotting

import matplotlib
matplotlib.use('Agg')
from matplotlib.pyplot import subplots

# Model Execution
def make_plot(file_obj):
    temp_obj = file_obj.variables['temp_mean']
    # store the temp_mean data in a variable
    temp = temp_obj[:]


    # use the subplots function to create a single plot
    # this makes things easier as you move to multipanel plotting
    fig, ax = subplots()

    # use the plot method of the axis object
    ax.plot(temp)

    # optional commands

    # # add gridlines to the plot
    ax.grid()

     # set limits for the x axis, 1440 total time values
    ax.set_xlim(0,1439)

     # add a title
    ax.set_title('Mean Temperature')

     # use the savefig function attached to the figure object, saving the figure
    fig.savefig('lineplot.png', dpi=300)

    return "Hello World Again!"
