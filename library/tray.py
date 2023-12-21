import pystray
import PIL.Image
from library import variable as vars

# image = PIL.Image.open('icon.ico')


def on_click(main_icon, item):
    if str(item) == 'Quit':
        print('Closing the app.')
        main_icon.stop()
        vars.run = False


# icon = pystray.Icon("name", image, "Auto Download Cleanup", menu=pystray.Menu(pystray.MenuItem("Quit", on_click)))


def start(icon_path):
    image = PIL.Image.open(icon_path)
    icon = pystray.Icon("name", image, "Auto Download Cleanup", menu=pystray.Menu(pystray.MenuItem("Quit", on_click)))
    icon.run_detached()
