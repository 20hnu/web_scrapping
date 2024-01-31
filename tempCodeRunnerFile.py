for img_tag in image_tags:
#     # Get the URL of the image from the 'src' attribute of the <img> tag
#     img_url = img_tag['src_url']

#     # Send an HTTP GET request to the image URL
#     img_response = requests.get(img_url)

#     # Extract the filename from the URL
#     filename = os.path.join(save_dir, os.path.basename(img_url))

#     # Save the image to the specified directory
#     with open(filename, 'wb') as f:
#         f.write(img_response.content)

#     print(f"Downloaded: {filename}")