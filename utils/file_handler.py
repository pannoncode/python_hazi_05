import json

from utils.params import json_folder, main_json_folder


def file_read_to_write(file_folder, file_name):
    with open(f"{file_folder}/{file_name}", "r",) as f_obj:
        data = json.load(f_obj)
        for item in data:
            file_name = item["Name"].replace(" ", "").replace("/", "")
            file_write(item, json_folder, file_name)


def file_write(item, json_path, json_name):
    with open(f"{json_path}/{json_name}.json", "w", encoding="utf-8") as f_obj:
        json.dump(item, f_obj, ensure_ascii=False, indent=4)


def file_reader(file_folder, file_name):
    data_list = []
    with open(f"{file_folder}/{file_name}", "r",) as f_obj:
        data = json.load(f_obj)
        for item in data:
            data_list.append(item)

    return data_list


def write_statistic_file(file_folder, file_name, statistic):
    with open(f"{file_folder}/{file_name}.json", "w", encoding="utf-8") as f_obj:
        json.dump(statistic, f_obj, ensure_ascii=False, indent=4)
