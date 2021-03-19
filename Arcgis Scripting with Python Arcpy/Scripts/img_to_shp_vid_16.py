import os
from PIL import Image, ExifTags

img_folder = r"D:\Files\GIS\_Tutorial\Data\imgs"
img_contents = os.listdir(img_folder)

for image in img_contents:

    full_path = os.path.join(img_folder, image)
    pil_img = Image.open(full_path)

    exif = {ExifTags.TAGS[k]: v for k, v in pil_img._getexif().items() if k in ExifTags.TAGS}
    print(exif)