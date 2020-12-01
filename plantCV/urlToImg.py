from urllib import request, error
import numpy as np
import cv2
import time


def urlToImg(url: str):
    while True:
        try:
            image = request.urlopen(url).read()
        except error.HTTPError:
            time.sleep(5)
        else:
            im_arr = np.frombuffer(image, dtype=np.uint8)  # im_arr is one-dim Numpy array
            img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
            return img
