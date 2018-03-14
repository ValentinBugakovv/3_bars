import argparse
import json
import os
from math import sqrt


def get_arguments():
    parser = argparse.ArgumentParser(description="Path to json file")
    parser.add_argument("file_path", help="Path to json file")
    args = parser.parse_args()
    return args


def get_bar_name(func):
    def warp(*args):
        return func(args[0])["properties"]["Attributes"]["Name"]

    return warp


def load_data(file_path):
    with open(file_path, "r", encoding="UTF-8") as json_file:
        return json.load(json_file)["features"]


@get_bar_name
def get_name_biggest_bar(bar_data):
    biggest_bar = max(
        bar_data,
        key=lambda bar:
        bar
        ["properties"]
        ["Attributes"]
        ["SeatsCount"]
    )
    return biggest_bar


@get_bar_name
def get_name_smallest_bar(bar_data):
    smallest_bar = min(
        bar_data,
        key=lambda bar:
        bar
        ["properties"]
        ["Attributes"]
        ["SeatsCount"]
    )
    return smallest_bar


@get_bar_name
def get_name_closest_bar(bar_data, longitude=55, latitude=37):
    closest_bar = min(
        bar_data,
        key=lambda bar:
        sqrt(
            (bar["geometry"]["coordinates"][0] - longitude) ** 2 +
            (bar["geometry"]["coordinates"][1] - latitude) ** 2
        )
    )
    return closest_bar


def main():
    try:
        file_path = get_arguments().file_path
        if os.path.isfile(file_path):
            bar_data = load_data(file_path)
        else:
            exit("This file does not exist")
    except FileNotFoundError:
        exit("This is not a json file")
    try:
        longitude = float(input("Введите долготу:\n"))
        latitude = float(input("Введите широту:\n"))
    except ValueError:
        exit("This is not numbers")
    biggest_bar = get_name_biggest_bar(bar_data)
    smallest_bar = get_name_smallest_bar(bar_data)
    closest_bar = get_name_closest_bar(bar_data, longitude, latitude)
    print("САМЫЙ БОЛЬШОЙ БАР:\n{}\n".format(biggest_bar))
    print("САМЫЙ МАЛЕНЬКИЙ БАР:\n{}\n".format(smallest_bar))
    print("САМЫЙ БЛИЗКИЙ БАР\n{}\n".format(closest_bar))


if __name__ == "__main__":
    main()
