import os
import shutil
import variable as var
import tray_icon as ti
def move_the_file_to_right_place(main_directory, move_folder, filename):
    if not os.path.exists(move_folder):
        os.makedirs(move_folder)
    shutil.move(os.path.join(main_directory, filename), os.path.join(move_folder, filename))
def check_file_extension(file_ext, dir, mov_dir, filename):
    if filename.endswith(file_ext):
        move_the_file_to_right_place(main_directory=dir, move_folder=mov_dir, filename=filename)
def main_stuff():
    print('Program started.')
    while var.run:
        for filename in os.listdir(var.directory):
            check_file_extension(".pdf", dir=var.directory, mov_dir=var.PDF, filename=filename)
            check_file_extension(".docx", dir=var.directory, mov_dir=var.DOCX, filename=filename)
            check_file_extension('.zip', dir=var.directory, mov_dir=var.ZIP, filename=filename)
            check_file_extension(tuple(var.Image), dir=var.directory, mov_dir=var.IMAGE, filename=filename)
            check_file_extension('.py', dir=var.directory, mov_dir=var.PYTHON, filename=filename)
            check_file_extension(tuple(var.Video), dir=var.directory, mov_dir=var.VIDEO, filename=filename)
            check_file_extension(tuple(var.audio_formats), dir=var.directory, mov_dir=var.MUSIC, filename=filename)
            check_file_extension('.torrent', dir=var.directory, mov_dir=var.TORRENT, filename=filename)


if __name__ == '__main__':
    ti.start()
    main_stuff()
