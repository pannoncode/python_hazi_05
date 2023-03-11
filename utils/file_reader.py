import json
import os

from params import json_folder, main_json_folder

file_path = "D:\Programozás\Suli\Prooktatás\Python\hazi\cars.json"

print(os.path.exists(json_folder))

def file_reader(file):
    print("OK")

def file_read_to_write(file):
    with open(f"{main_json_folder}\cars.json", "r",) as f_obj:
        data = json.load(f_obj)
        for item in data:
            file_name = item["Name"].replace(" ", "").replace("/", "-")
            file_write(item, json_folder, file_name)
        

def file_write(item, json_path, json_name):
    with open(f"{json_path}\{json_name}.json", "w", encoding="utf-8") as f_obj:
        json.dump(item, f_obj, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    print("ok")
    file_read_to_write(file_path)