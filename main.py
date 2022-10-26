import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

page = requests.get("https://statsroyale.com/cards")
souped = BeautifulSoup(page.content,"html.parser")
imgs = souped.find_all("img")
imgs = imgs[3:-1]

for img in tqdm(imgs):
    imglink = img.attrs.get("src")
    image=requests.get(imglink).content
    filename = r"C:\Python\cards"+imglink[imglink.rfind("/"):]
    with open(filename,"wb") as file:
        file.write(image)
