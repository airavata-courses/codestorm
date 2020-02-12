from auth import authenticate
from datetime import datetime
import configparser
from imgurpython import ImgurClient

# config = configparser.Configparser()
# config.read('auth.ini')
#
# config_id = config.get('credentials', 'client_id')
# client_secret = config.get('credentials', 'client_secret')

# client = ImgurClient(client_id, client_secret)
image_path = 'test1.jpeg'

def upload_image(client):
    config = {
    title = image_path
    }
    print("Uploading image!!!")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done!!!!"")
    print(image)
    return image

if __name__ == "__main__"
    client = authenticate()
    image = upload_image(client)
    print(  image['link'])
