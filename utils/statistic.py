import datetime
from utils.params import main_json_folder, statistic_folder
from utils.file_handler import file_reader, write_statistic_file


def high_horsepower(file):
    horse_power_min = 0
    horse_power_result = {}
    for item in file:
        if item["Horsepower"] is not None and item["Horsepower"] > horse_power_min:
            horse_power_result = {
                "car_name": item["Name"],
                "horse_power": item["Horsepower"]
            }
            horse_power_min = item["Horsepower"]
    return horse_power_result


def old_car(file):
    begin_date = datetime.datetime.strptime('2100-01-01', "%Y-%m-%d").date()
    old_car_result = {}
    for item in file:
        if item["Year"] is not None:
            car_date = datetime.datetime.strptime(
                item["Year"], "%Y-%m-%d").date()
            if car_date < begin_date:
                old_car_result = {
                    "name": item["Name"],
                    "year": item["Year"]
                }
                begin_date = car_date
    return old_car_result


def new_car(file):
    begin_date = datetime.datetime.strptime('1900-01-01', "%Y-%m-%d").date()
    new_car_result = {}
    for item in file:
        if item["Year"] is not None:
            car_date = datetime.datetime.strptime(
                item["Year"], "%Y-%m-%d").date()
            if car_date > begin_date:
                new_car_result = {
                    "name": item["Name"],
                    "year": item["Year"]
                }
                begin_date = car_date
    return new_car_result


def generate_statistic():
    data = file_reader(main_json_folder, "cars.json")

    horsepower = high_horsepower(data)
    oldcar = old_car(data)
    newcar = new_car(data)

    statistic = {
        "high_horsepower": horsepower,
        "old_car": oldcar,
        "new_car": newcar
    }

    write_statistic_file(statistic_folder, "statistics", statistic)
