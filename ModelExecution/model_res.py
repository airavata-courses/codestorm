from auth import authenticate
from datetime import datetime
import configparser
from imgurpython import ImgurClient

config = configparser.ConfigParser()
config.read('auth.ini')

client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')

client = ImgurClient(client_id, client_secret)
image_path = 'lineplot.png'

def upload_image(client):
    print("Uploading image!!!")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done!!!!")
    print(image)
    return image

def helper():
    image = upload_image(client)
    image_link = image['link']
    return image_link