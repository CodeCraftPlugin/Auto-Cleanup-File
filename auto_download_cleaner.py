import os
import shutil
import variable as var
import save as sv
import tray_icon as ti
import time as time
def move_file(main_directory, move_folder, filename):
    if not os.path.exists(move_folder):
        os.makedirs(move_folder)
    shutil.move(os.path.join(main_directory, filename), os.path.join(move_folder, filename))
def check_file_extension(file_ext, mov_dir, filename):
    if filename.endswith(file_ext):
        time.sleep(1)
        move_file(main_directory=sv.get_default_download_folder(), move_folder=mov_dir, filename=filename)
def main_stuff():
    loaded_vars = sv.load_variables_from_json()
    print(loaded_vars)
    print(sv.get_default_download_folder())
    print(loaded_vars['DOCX'])
    print('Program started.')
    while var.run:
        for filename in os.listdir(sv.get_default_download_folder()):
            try:
                check_file_extension(".pdf",  mov_dir=loaded_vars[var.PDF], filename=filename)
                check_file_extension(".docx",  mov_dir=loaded_vars[var.DOCX], filename=filename)
                check_file_extension('.zip',  mov_dir=loaded_vars[var.ZIP], filename=filename)
                check_file_extension(var.Image,  mov_dir=loaded_vars[var.IMAGE], filename=filename)
                check_file_extension('.py',  mov_dir=loaded_vars[var.Python], filename=filename)
                check_file_extension(var.Video,  mov_dir=loaded_vars[var.VIDEO], filename=filename)
                check_file_extension(var.audio_formats,  mov_dir=loaded_vars[var.MUSIC], filename=filename)
                check_file_extension('.torrent',  mov_dir=loaded_vars[var.Torrent], filename=filename)
            except PermissionError:
                continue
if __name__ == "__main__":
    sv.main()
    ti.start()
    main_stuff() 
