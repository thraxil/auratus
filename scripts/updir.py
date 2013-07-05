#!ve/bin/python
import requests
import os
import sys

abase = sys.argv[1]
d = sys.argv[2]

images = os.listdir(d)
images.sort()
for i in images:
    if not i.lower().endswith('jpg'):
        continue
    print i
    files = {'image':
                 (i,
                  open(os.path.join(d, i)))
             }
    r = requests.post(abase + "add_photo/", files=files)

