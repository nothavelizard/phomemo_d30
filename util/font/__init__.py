import os
import requests
import re
from fontTools.ttLib import TTFont
from PIL import ImageFont

MODULEFOLDER = os.path.dirname(__file__)
FONTFOLDER = os.path.join(MODULEFOLDER, "ttf")
LIST_AVAILABLE = os.listdir(FONTFOLDER)

# print(FONTFOLDER)
def request_font(name):
    """
    Fetches a TTF version of a Google Font by name.
    """
    url = f"https://fonts.googleapis.com/css?family={name}"
    response = requests.get(url)
    match = re.search(r'src: url\((.*.ttf)', response.text)
    font_url = match.group(1)
    return requests.get(font_url).content

def save_font(name):
    font = request_font(name)
    with open(f"{FONTFOLDER}/{name}.ttf", "wb") as f:
        f.write(font)

def get_font(name):
    if f"{name}.ttf" not in os.listdir(FONTFOLDER):
        save_font(name)
        return ImageFont.truetype(f"{FONTFOLDER}/{name}.ttf")
    return ImageFont.truetype(f"{FONTFOLDER}/{name}.ttf")

def load_font(name):
    get_font(name)

DEFAULT = get_font("Roboto")