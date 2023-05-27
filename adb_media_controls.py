from pynput import *
from pynput.keyboard import Key 
from ppadb.client import Client 
client = Client(host="127.0.0.1", port=5037)
device = client.device("10.0.0.181:5555")
print('AndroidTV ADB MEDIA controls Press ESC to exit')
print('     ↑ Vol+ ')
print('N/A←   →play/pause')
print('     ↓vol-')
def on_key_release(key):
    if key == Key.right:
        device.shell("input keyevent 85")
        print("play/pause")
    elif key == Key.left:
        print("Left key clicked")
    elif key == Key.up:
        device.shell("input keyevent 24")
        print("Volume up")
    elif key == Key.down:
        device.shell("input keyevent 25")
        print("Volume down")
    elif key == Key.esc:
        exit()


with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
