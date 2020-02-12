# importing reuired libraries
from flask import Flask
from flask_cors import CORS,cross_origin
from netCDF4 import Dataset
import generate_plot as gp
# must insert this statement to render the plots within the notebook
# this is specific to the ipython notebook
#%matplotlib inline
# import subplots function for plotting
import matplotlib
matplotlib.use('Agg')
from matplotlib.pyplot import subplots


# initializing flask application
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

# enabling cross origin access to any source
# Once the applciation is deployed, the '*' will be replaced with
# source URL
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})




@app.route("/hello")
def retrieve_data():
    # Path to netCDF file, change /data_path/ to match where the file is located on your system
    file_name = 'sgpmetE13.b1.20140218.000000.cdf'

    # use the Dataset function to create an object reference to the open netCDF file
    file_obj = Dataset(file_name)

    # printing the file object displays the python type, global attributes, file dimensions, 
    # and variables in the file
    print(file_obj)

    gp.make_plot(file_obj)


    return "Hello World!!!"
# def make_plot(file_obj):
#     temp_obj = file_obj.variables['temp_mean']
#     # store the temp_mean data in a variable
#     temp = temp_obj[:]
    

#     # use the subplots function to create a single plot 
#     # this makes things easier as you move to multipanel plotting
#     fig, ax = subplots()

#     # use the plot method of the axis object
#     ax.plot(temp)

#     # # optional commands

#     # # add gridlines to the plot
#     ax.grid()

#     # # set limits for the x axis, 1440 total time values
#     ax.set_xlim(0,1439)

#     # # add a title
#     ax.set_title('Mean Temperature')

#     # # use the savefig function attached to the figure object, saving the figure 
#     fig.savefig('lineplot.png', dpi=300)

#     return "Hello World Again!"

# retrieve_data()

# # Starting the application server
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 6000)



