# importing reuired libraries
from flask import Flask
from flask_cors import CORS,cross_origin

# initializing flask application
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

# enabling cross origin access to any source
# Once the applciation is deployed, the '*' will be replaced with
# source URL
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/hello")
def hello():
    return "Hello World@@@@!!!"


# Starting the application server
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5001)
