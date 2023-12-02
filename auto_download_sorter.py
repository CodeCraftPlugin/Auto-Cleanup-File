import os
import shutil
import variable as var
import tray_icon as ti
import save as sv
import time as time
import json


def load_variables_from_json():
    dirname = os.path.join(os.getenv("APPDATA"), "Auto-Download-Cleaner")
    filename = os.path.join(dirname, 'config.json')
    try:
        with open(filename, "r") as json_file:
            loaded_vars = json.load(json_file)
    except FileNotFoundError:
        # If the config file doesn't exist, return an empty dictionary
        return {}
    return loaded_vars


def move_file(main_directory, move_folder, filename):
    if move_folder is None:
        raise ValueError("Invalid move_folder: None")

    if not os.path.exists(move_folder):
        os.makedirs(move_folder)

    shutil.move(os.path.join(main_directory, filename), os.path.join(move_folder, filename))


def check_file_extension(file_ext, mov_dir, filename):
    if filename.endswith(file_ext):
        time.sleep(1)
        move_file(main_directory=sv.get_default_download_folder(), move_folder=mov_dir, filename=filename)


def main_stuff():
    sv.main()
    loaded_vars = load_variables_from_json()
    print(loaded_vars)
    print(sv.get_default_download_folder())
    print('Program started.')
    while var.run:
        print("running")
        try:
            folder_content = os.listdir(sv.get_default_download_folder())
        except PermissionError:
            continue
        for filename in folder_content:
            check_file_extension(".pdf", mov_dir=loaded_vars.get(var.PDF), filename=filename)
            check_file_extension(".docx", mov_dir=loaded_vars.get(var.DOCX), filename=filename)
            check_file_extension(var.Zip, mov_dir=loaded_vars.get(var.ZIP), filename=filename)
            check_file_extension(var.Image, mov_dir=loaded_vars.get(var.IMAGE), filename=filename)
            check_file_extension('.py', mov_dir=loaded_vars.get(var.Python), filename=filename)
            check_file_extension(var.Video, mov_dir=loaded_vars.get(var.VIDEO), filename=filename)
            check_file_extension(var.audio_formats, mov_dir=loaded_vars.get(var.MUSIC), filename=filename)
            check_file_extension('.torrent', mov_dir=loaded_vars.get(var.Torrent), filename=filename)
        time.sleep(0.5)


if __name__ == "__main__":
    ti.start()
    main_stuff()
