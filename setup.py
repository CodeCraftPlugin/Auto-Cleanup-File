from cx_Freeze import setup, Executable
import sys
import os
version = 'v1.2.0'


# os.system(f"echo '::set-output name=version::{version}'")
# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ['os', 'getpass', 'library','pystray'], 'excludes': [], 'build_exe': 'build_windows',
                 'include_files': ['icon.ico', 'README.md', 'LICENSE.md', 'icon.jpg']}

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('auto_download_sorter.py', base=base, target_name='Auto Download Sorter', icon='icon.ico')
]

setup(name='Auto Download Sorter',
      version=version,
      description='Auto Download Sorter',
      options={'build_exe': build_options},
      executables=executables,
      author='CodeCraftPlugin',
      author_email='behl8948@gmail.com',
      license='MIT')
