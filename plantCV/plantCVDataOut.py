from plantcv.plantcv import outputs


def print_results():
    observations = outputs.observations
    keyList = ["blue_frequencies", "green_frequencies", "red_frequencies", "lightness_frequencies",
               "green-magenta_frequencies", "blue-yellow_frequencies", "hue_frequencies", "saturation_frequencies",
               "value_frequencies"]

    returnList = {}
    for key in keyList:
        returnList[key] = cleaner(observations[key])

    return returnList


def cleaner(list):
    returnList = {
        "value": list["value"],
        "label": list["label"]
    }
    return returnList
