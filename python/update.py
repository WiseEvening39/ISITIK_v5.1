import requests
import pymupdf

import os
from os import path

PDF_URL = "https://docs.cspu.ru/raspisanie-zanyatiy/och/fizmat(Inf)/Raspisanie/1k.pdf"
PDF_FILENAME = "full_schedule.pdf"
IMG_FULLPATH = path.join(os.getcwd(), "img", "schedule.png")

r = requests.get(PDF_URL)

if (r.status_code != 200):
    print(f"Error status code: {r.status_code}:\n{r.text}")
    quit()

with open(PDF_FILENAME, "wb") as f:
    f.write(r.content)
    print("pdf saved")

schedule_pdf = pymupdf.open(PDF_FILENAME)
out_image = schedule_pdf[1].get_pixmap()
out_image.save(IMG_FULLPATH)

print("image saved")

