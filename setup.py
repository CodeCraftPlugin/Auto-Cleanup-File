from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [],'build_exe': 'build_windows'}

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, target_name = 'Auto-Download-Cleanup',uac_admin=True,icon='icon.ico')
]

setup(name='Auto-Download-Cleanup',
      version = '1.0',
      description = 'Automatic sorter for downloads folder',
      options = {'build_exe': build_options},
      executables = executables)
