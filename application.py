from flask import Flask, request, jsonify,json
from plantCV.urlToImg import urlToImg
from plantCV.plantCVModule import plantCVProcess
application = Flask(__name__)


@application.route('/', methods=['POST','GET'])
def PlantCV():

    if request.method == "post":
        form = json.loads(request.data)
        if "imageURL" not in form or "roi" not in form:
            return "Invalid", 422

        imageURL = form["imageURL"]
        roi = form["roi"]

        if not isinstance(roi, dict):
            return "Invalid", 422

        if "x" not in roi or "y" not in roi or "w" not in roi or "h" not in roi:
            return "Invalid", 422

        x = roi["x"]
        y = roi["y"]
        w = roi["w"]
        h = roi["h"]

        img = urlToImg(imageURL)
        return plantCVProcess(img, x, y, w, h), 200
    else:
        return "getTest", 200


if __name__ == '__main__':
    application.run()
