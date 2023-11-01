import time
from random import randint
from concurrent.futures import ThreadPoolExecutor
import requests
from flask import Flask

app = Flask(__name__)

img_list_count = 10

@app.route('/')
def hello_world():
    return 'Hello World!'

def get_xkcd_image(random):
    response = requests.get(f'https://xkcd.com/{random}/info.0.json')
    return response.json()['img']

def get_multiple_images(number):
    with ThreadPoolExecutor() as executor:
        random_numbers = [randint(0, 300) for _ in range(number)]
        urls = list(executor.map(get_xkcd_image, random_numbers))
    return urls

@app.route('/comic')
def hello():
    start = time.perf_counter()
    urls = get_multiple_images(img_list_count)
    end = time.perf_counter()
    markup = f"Time taken: {end-start}<br><br>"
    for url in urls:
        markup += f'<img src="{url}"></img><br><br>'
    return markup

if __name__ == '__main__':
    app.run(debug=True)
