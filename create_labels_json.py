import sys
import json


def main():

    labels = {
        "0"  : "Anime",
        "1"  : "Cartoon",
    }

    json.dump(labels, open("labels.json", "w"))


if __name__ == "__main__":
    sys.exit(main() or 0)