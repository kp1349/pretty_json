# By Koushik Paul (kp1349)

import os
import json

from glob import glob


# CREATE NEW FOLDER
current_working_directory = os.getcwd()
new_folder_name = "pretty_json"

# this is to make sure it's OS agnostic
new_path = os.path.join(current_working_directory, new_folder_name)

if not os.path.exists(new_path):  # check if the folder is already there
    os.makedirs(new_path)  # create it

# LOOP THROUGH EVERY JSON FILE IN THE DIRECTORY
json_file_extension = "*.json"  # we want to find every json file
json_input_path = os.path.join(current_working_directory, json_file_extension)
for json_file_path in glob(json_input_path):
    json_file_name = os.path.basename(json_file_path)  # get the file name
    print("reading file: {}".format(json_file_name))  # DEBUG

    # open the file, parse it, 'prettify' it, save it to string
    json_file_descriptor = open(json_file_path, "r")  # read-only
    parsed_json_string = json.load(json_file_descriptor)
    pretty_json = json.dumps(parsed_json_string, indent=4, sort_keys=True)

    # create new file and write the 'pretty' json to it
    new_file_name = json_file_name
    new_file_path = os.path.join(new_path, new_file_name)
    new_file_descriptor = open(new_file_path, "w+")
    new_file_descriptor.write(pretty_json)

# TODO: ADD A PROGRESS BAR