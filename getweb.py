import requests
from PIL import Image

# get form web
def getImg(imgPath):
    return Image.open(requests.get(imgPath,stream=True).raw)