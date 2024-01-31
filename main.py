from bs4 import BeautifulSoup
import requests
import urllib.parse

url = "https://www.nepalhikingteam.com/world-heritage-sites-of-nepal"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

def source():
    decoded_urls = []
    image_tags = soup.find_all('img')
    for tag in image_tags:
        src_url_encoded = tag['src']
        src_url = urllib.parse.unquote(src_url_encoded)
        index1 = src_url.find('=')
        index2 = src_url.find('&')
        if index1 != -1 and index2 != -1:
            sliced_url = src_url[index1+1:index2]
        else:
            sliced_url = src_url
        decoded_urls.append(sliced_url)
    
    return decoded_urls
