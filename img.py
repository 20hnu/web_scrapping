import requests
import os
from main import source

# Make a GET request to download the image
urls = source()

for item in urls:
    print(item)
    response = requests.get(item)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        filename = os.path.join("images",os.path.basename(item))
        with open(filename,'wb') as f:
            f.write(response.content)
    else:
        break
        # print("Failed to download image. Status code:", response.status_code)
                     