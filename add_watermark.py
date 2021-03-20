import sys
import glob
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def add_watermark(query_str):
    """
    This function adds watermarks for the images downloaded matching the query string.
    :param query_str: The query string used to download images.  Example: cars, apples, ...
    """
    images = glob.glob("/Users/britneyf/foundations_in_software_engineering/bing_image_downloader/dataset/" + query_str
                       + "/*.jpg")

    for image in images:
        with open(image, 'rb') as file:
            img = Image.open(file)
            draw = ImageDraw.Draw(img)

            font = ImageFont.truetype("Georgia Bold", 20)

            text = 'MY WATERMARK'
            draw.text((66, 120), text, font=font, fill="black")
            img.save(image)


if __name__ == '__main__':
    query_str = sys.argv[1]
    add_watermark(query_str)
