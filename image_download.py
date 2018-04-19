# /*
# import csv
# with open('photo_links.csv', newline='') as f:
#     reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
#     for row in reader:
#         print(row)
#
# */

import csv

prefix_url = 'http://cse.sust.edu/reunion'
url = 'http://cse.sust.edu/reunion/photos/1523235087426087.jpg'
path = 'image1.png'

with open('photo_links.csv', "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print " ---> " + prefix_url + row[2]


import requests
import shutil

r = requests.get(url, stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
