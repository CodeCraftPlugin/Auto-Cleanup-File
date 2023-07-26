import os
import shutil

run = True
directory = 'C:\\Users\\CodeCraft\\Downloads'
PDF = 'C:\\Users\\CodeCraft\\Documents\\PDF'
DOCX = 'C:\\Users\\CodeCraft\\Documents\\DOC'
TORRENT = 'C:\\Users\\CodeCraft\\Downloads\\TORRENT'
ZIP = 'D:\\Zip'
Image = ['.png', '.jpg', '.jpeg', '.gif', '.tiff', '.psd', '.raw', '.bmp', '.heif', '.indd', '.svg', '.ai', '.eps', '.pdf', '.ico', '.webp']
IMAGE = 'C:\\Users\\CodeCraft\\Pictures\\Photos'
PYTHON = 'D:\\Python'
VIDEO = 'C:\\Users\\CodeCraft\\Videos'
MUSIC = 'C:\\Users\\CodeCraft\\Music'
Video = ['.mp4', '.mov', '.wmv', '.avi', '.avchd', '.flv', '.f4v', '.swf', '.mkv', '.webm', '.mng', '.gifv', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.ogg', '.m4p', '.m4v', '.wmv', '.mov', '.qt', '.flv', '.swf', '.avchd']
audio_formats = ('.mp3', '.wav', '.aiff', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.ape', '.alac', '.dsd')
def move_the_file_to_right_place(main_directory, move_folder, filename):
    if not os.path.exists(move_folder):
        os.makedirs(move_folder)
    shutil.move(os.path.join(main_directory, filename), os.path.join(move_folder, filename))

def check_file_extension(file_ext, dir, mov_dir, filename):
    if filename.endswith(file_ext):
        move_the_file_to_right_place(main_directory=dir, move_folder=mov_dir, filename=filename)

try:
    print('Program started.')
    print('Please press Crtl C to close the app.')
    while run:
        for filename in os.listdir(directory):
            check_file_extension(".pdf", dir=directory, mov_dir=PDF, filename=filename)
            check_file_extension(".docx", dir=directory, mov_dir=DOCX, filename=filename)
            check_file_extension('.zip', dir=directory, mov_dir=ZIP, filename=filename)
            check_file_extension(tuple(Image), dir=directory, mov_dir=IMAGE, filename=filename)
            check_file_extension('.py', dir=directory, mov_dir=PYTHON, filename=filename)
            check_file_extension(tuple(Video), dir=directory, mov_dir=VIDEO, filename=filename)
            check_file_extension(tuple(audio_formats), dir=directory, mov_dir=MUSIC, filename=filename)
            check_file_extension('.torrent', dir=directory, mov_dir=TORRENT, filename=filename)
except KeyboardInterrupt:
    print('Closing the app.')
    # Do some stuff here, such as saving data or cleaning up resources.