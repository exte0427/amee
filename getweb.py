import requests
from PIL import Image
def getImg(imgPath):
    return Image.open(requests.get(imgPath,stream=True).raw)