import io
import re
import requests
import font
from PIL import Image, ImageDraw, ImageFont

SELECTED_FONT = font.load_font("Roboto")

def generate_text_image(text, filename):
    """
    Generates an image with centered text using a Google Font (Roboto here).
    The canvas is then extended and rotated 270°, and saved to disk.
    """
    font_size = 24
    font = SELECTED_FONT
    width, height = 288, 88
    
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    draw.text((width/2,height/2), text, font=font, fill="black", font_size=font_size, anchor='mb')
    extended_width, extended_height = 320, 96
    extended_img = Image.new("RGB", (extended_width, extended_height), "white")
    offset_x = (extended_width - width) // 2
    offset_y = (extended_height - height) // 2
    extended_img.paste(img, (offset_x, offset_y))
    rotated_img = extended_img.rotate(270, expand=True, fillcolor="white")
    rotated_img.save(filename)
    return filename
