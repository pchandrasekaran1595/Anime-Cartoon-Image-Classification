import sys
import json


def main():

    labels = {
        "0"  : "Dew",
        "1"  : "Fog Smog",
        "2"  : "Frost",
        "3"  : "Glaze",
        "4"  : "Hail",
        "5"  : "Lightning",
        "6"  : "Rain",
        "7"  : "Rainbow",
        "8"  : "Rime",
        "9"  : "Sandstorm",
        "10" : "Snow"
    }

    json.dump(labels, open("labels.json", "w"))


if __name__ == "__main__":
    sys.exit(main() or 0)