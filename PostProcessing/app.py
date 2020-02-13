# importing reuired libraries
from flask import Flask
from flask_cors import CORS,cross_origin
import post_processing_consumer as ppc

# initializing flask application
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

# enabling cross origin access to any source
# Once the applciation is deployed, the '*' will be replaced with
# source URL
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/postprocessing")
def helper():
    #Response is already in pickled format. Hence, returning it as it is.
    image_link = ppc.pp_consumer()
    print("Got link object in the helper of app.py of post processing!!!!! ------> ", image_link)
    return image_link

# Starting the application server
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5500)
