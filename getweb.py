import requests
from PIL import Image,ImageTk
def getImg(imgPath):
    return Image.open(requests.get(imgPath,stream=True).raw)