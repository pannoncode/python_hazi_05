from utils.file_handler import file_read_to_write
from utils.statistic import generate_statistic
from utils.params import main_json_folder

file_read_to_write(main_json_folder, "cars.json")
generate_statistic()
