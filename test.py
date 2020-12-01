import base64
from urllib import request, error
import numpy as np
import cv2
import time

import requests
import json

while True:
    try:
        image = request.urlopen("https://aednoriginalimage.s3.amazonaws.com/1606768299700/1606768356.jpg").read()
    except error.HTTPError:
        time.sleep(5)
    else:
        im_arr = np.frombuffer(image, dtype=np.uint8)  # im_arr is one-dim Numpy array
        img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
        cv2.imwrite("out.jpg", img)
        break
