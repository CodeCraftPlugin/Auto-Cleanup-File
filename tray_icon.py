import pystray
import PIL.Image
import variable as vars

image = PIL.Image.open("icon.ico")

def on_click(icon, item):
    if str(item) == 'Quit':
        print('Closing the app.')
        icon.stop()
        vars.run = False

icon = pystray.Icon("name", image, "Auto Download Cleanup", menu=pystray.Menu(pystray.MenuItem("Quit", on_click)))
def start():
    icon.run_detached()
