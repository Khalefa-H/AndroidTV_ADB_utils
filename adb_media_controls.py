from pynput import *
from pynput.keyboard import Key 
from ppadb.client import Client 
# Device name
chromecast_name=""
#adb Server 
client = Client(host="127.0.0.1", port=5037)
device = client.device(chromecast_name)
#Infomation
print('AndroidTV ADB MEDIA controls Press ESC to exit')
print('     ↑ Vol+ ')
print('N/A←   →play/pause')
print('     ↓vol-')
#Listener
def on_key_release(key):
    if key == Key.right:
        device.shell("input keyevent 85")
       
    elif key == Key.left:
      
    elif key == Key.up:
        device.shell("input keyevent 24")
        
    elif key == Key.down:
        device.shell("input keyevent 25")
        
    elif key == Key.esc:
        exit()

#start Listening
with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
