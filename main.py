from enum import Enum
from watermark import File, Watermark, apply_watermark, Position
from PIL import Image
import os
from dataclasses import dataclass

# photo = File('Screenshot from 2022-11-16 14-57-18.png')
# watermark = Watermark(File("watermark.png"), pos=Position.bottom_right)
# apply_watermark(photo, watermark)



# Bulk watermark
def bulkWaterMark(srcFolder: str) -> str:
    images = os.listdir(srcFolder)
    for img in images:
        watermark = Watermark(File('watermark.png'), pos=Position.bottom_right)
        gh = apply_watermark(File(img), watermark)
        print(gh)
        # learn to create a directory and save watermarked images inside it.
        outputFolder = "watermarked"
        if not os.path.exists(outputFolder):
            os.makedirs(outputFolder)
        Image.SAVE(outputFolder, img)
bulkWaterMark('images')