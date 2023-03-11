import os

json_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "json_files")
main_json_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "main_json_file")

print(os.path.exists(main_json_folder))
