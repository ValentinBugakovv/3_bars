import argparse
import json
from math import sqrt


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Path to json file"
    )
    parser.add_argument(
        "filepath",
        help="Path to json file",
    )
    args = parser.parse_args()
    return args


def pretty_print_json(func):
    def wrap(*args):
        return json.dumps(func(args[0]),
                          sort_keys=True,
                          indent=4,
                          ensure_ascii=False,
                          separators=(",", ": ")
                          )

    return wrap


def load_data(filepath):
    with open(filepath, "r", encoding="UTF-8") as json_file:
        return json.load(json_file)


@pretty_print_json
def get_attributes_biggest_bar(bar_data):
    biggest_bar = max(
        bar_data["features"], key=lambda bar:
        bar["properties"]["Attributes"]["SeatsCount"]
    )
    attributes = biggest_bar["properties"]["Attributes"]
    return attributes


@pretty_print_json
def get_attributes_smallest_bar(bar_data):
    smallest_bar = min(
        bar_data["features"], key=lambda bar:
        bar["properties"]["Attributes"]["SeatsCount"]
    )
    attributes = smallest_bar["properties"]["Attributes"]
    return attributes


@pretty_print_json
def get_attributes_closest_bar(bar_data, longitude=37.55, latitude=55.75):
    closest_bar = min(
        bar_data["features"], key=lambda bar: sqrt(
            (bar["geometry"]["coordinates"][0] - longitude) ** 2 +
            (bar["geometry"]["coordinates"][1] - latitude) ** 2)
    )
    attributes = closest_bar["properties"]["Attributes"]
    return attributes


def main():
    try:
        file_path = get_arguments().filepath
        bar_data = load_data(file_path)
    except ValueError:
        print("This is not a json file")
        exit()
    try:
        longitude = float(input("Введите долготу:\n"))
        latitude = float(input("Введите широту:\n"))
    except ValueError:
        print("This is not numbers")
        exit()
    biggest_bar = get_attributes_biggest_bar(bar_data)
    smallest_bar = get_attributes_smallest_bar(bar_data)
    closest_bar = get_attributes_closest_bar(bar_data, longitude, latitude)
    print("INFORMATION ABOUT THE BIGGEST BAR\n", biggest_bar, end=3 * "\n")
    print("INFORMATION ABOUT THE SMALLEST BAR\n", smallest_bar, end=3 * "\n")
    print("INFORMATION ABOUT THE CLOSEST BAR\n", closest_bar)


if __name__ == "__main__":
    main()
