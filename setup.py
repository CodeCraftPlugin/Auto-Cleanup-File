from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [],'build_exe': 'build_windows'}

base = 'console'

executables = [
    Executable('main.py', base=base, target_name = 'Auto-Download-Cleanup',uac_admin=True,icon='icon.ico')
]

setup(name='Auto-Download-Cleanup',
      version = '1.0',
      description = 'Automatic sorter for downloads folder',
      options = {'build_exe': build_options},
      executables = executables)
