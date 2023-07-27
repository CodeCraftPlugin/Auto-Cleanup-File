from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [],'build_exe': 'build_windows','include_files':['icon.ico']}

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('auto_download_cleaner.py', base=base, target_name = 'Auto-Download-Cleanup',icon='icon.ico')
]

setup(name='Auto-Download-Cleanup',
      version = '1.0',
      description = 'Automatic sorter for downloads folder',
      options = {'build_exe': build_options},
      executables = executables)
