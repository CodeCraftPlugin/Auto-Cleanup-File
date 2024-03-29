import os
import json
import getpass

from library import variable


def get_default_download_folder():
    # try to automatically detect the download folder
    default_download_folder = None

    # Platform-specific logic to detect the download folder
    if os.name == "posix":  # Linux/Mac
        default_download_folder = os.path.expanduser("~/Downloads")
    elif os.name == "nt":  # Windows
        default_download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        print("Unsupported operating system.")
        exit(1)

    return default_download_folder


def create_default_directories():
    # If username is "codecraft", use the hardcoded download folder this is for my personal use
    username = getpass.getuser()
    if username == "CodeCraft":
        default_dirs = default_dirs = {
            "PDF": os.path.join(os.path.expanduser("~"), "Documents", "PDF"),
            "DOCX": os.path.join(os.path.expanduser("~"), "Documents", "DOCX"),
            "ZIP": variable.ZIP_DIR,
            "Image": os.path.join(os.path.expanduser("~"), "Pictures", "Photos"),
            "Python": variable.PYTHON_DIR,
            "Video": os.path.join(os.path.expanduser("~"), "Videos"),
            "Music": os.path.join(os.path.expanduser("~"), "Music"),
            "Torrent": os.path.join(get_default_download_folder(), "Torrents")
        }
        return default_dirs
    # Define default directories for different file types
    default_dirs = {
        "PDF": os.path.join(os.path.expanduser("~"), "Documents", "PDF"),
        "DOCX": os.path.join(os.path.expanduser("~"), "Documents", "DOCX"),
        "ZIP": os.path.join(get_default_download_folder(), "ZIP"),
        "Image": os.path.join(os.path.expanduser("~"), "Pictures", "Photos"),
        "Python": os.path.join(os.path.expanduser("~"), "Code", "Python"),
        "Video": os.path.join(os.path.expanduser("~"), "Videos"),
        "Music": os.path.join(os.path.expanduser("~"), "Music"),
        "Torrent": os.path.join(get_default_download_folder(), "Torrents")
    }

    return default_dirs


def save_variables_to_json(vars_dict):
    appdata = os.getenv("APPDATA")
    app_config = os.path.join(appdata, "Auto-Download-Sorter")
    if not os.path.exists(app_config):
        os.makedirs(app_config)
    filename = os.path.join(app_config, "config.json")
    if not os.path.exists(filename):
        with open(filename, "w") as json_file:
            json.dump(vars_dict, json_file, indent=4)


def main():
    username = getpass.getuser()
    # Create default directories for different file types
    default_directories = create_default_directories()

    # Save the variables to a JSON file
    if not (os.path.exists("config.json")):
        save_variables_to_json(default_directories)
