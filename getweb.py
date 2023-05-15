import requests
import random
from PIL import Image

ameList = [
        "https://yt3.googleusercontent.com/RZ4Fp3L6_zyq6YA7s5WnH8-22iezMLwdJhtkBgs_EAb06mvMCnF59JKMNu9YPCqb7nhaeXMdPvY=s176-c-k-c0x00ffffff-no-rj",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4unk7PB3cGWuVnm9rTdH-JYW3oOmbOXmQag&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQctlsxhIXQXsbrh8g46RYJ5wZFGO52Q2LYOA&usqp=CAU",
]

class AmeImg:
    def __init__(self):
        self.ameList = list(map(_getImg,ameList))
        
    def get(self):
        return self.ameList[random.randint(0,len(self.ameList)-1)]

# get form web
def _getImg(imgPath):
    return Image.open(requests.get(imgPath,stream=True).raw)