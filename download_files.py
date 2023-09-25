import requests

url = 'https://media.istockphoto.com/id/1322277517/pl/zdj%C4%99cie/dzika-trawa-w-g%C3%B3rach-o-zachodzie-s%C5%82o%C5%84ca.webp?s=2048x2048&w=is&k=20&c=-ziXJQaUGQtzBL_0PEvq13Cg_B3FkO4quD2rYXb3Mr0='

# make a request
response = requests.get(url)

with open('image.jpg', 'wb') as file:
    file.write(response.content)

