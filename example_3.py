import os
from pathlib import Path

JPEG_FILE_PATH = Path("files") / "example.jpeg"
OUTPUT_FILE_PATH = Path("files") / "example_out.jpeg"

with open(JPEG_FILE_PATH, "rb") as f_in, \
     open(OUTPUT_FILE_PATH, "wb") as f_out:

    img = f_in.read()
    f_out.write(img)

with open(OUTPUT_FILE_PATH, "rb") as new_file:
    img_res = new_file.read()

assert img == img_res


if os.path.exists(OUTPUT_FILE_PATH):
    os.remove(OUTPUT_FILE_PATH)

assert not OUTPUT_FILE_PATH.exists()


