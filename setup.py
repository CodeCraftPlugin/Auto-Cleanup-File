from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ['os', 'getpass', 'library'], 'excludes': [], 'build_exe': 'build_windows',
                 'include_files': ['icon.ico', 'README.md', 'Licence.md', 'icon.jpg']}

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('auto_download_sorter.py', base=base, target_name='Auto Download Sorter', icon='icon.ico')
]
setup(name='Auto Download Sorter',
      version='1.0',
      description='Auto Download Sorter',
      options={'build_exe': build_options},
      executables=executables)
