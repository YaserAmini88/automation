from watchdog import observers
from watchdog.events import FileSystemEventHandler
import json
import os
import time

class FileHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(home):
            source = home +"/"+ filename
            new_folder = destination +"/"+ filename
            os.rename(source, new_folder)

directory = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
home = "C:\\Users\\Yaser\\Desktop\\newfolder"
destination = "C:\\Users\\Yaser\\Desktop\\newfolder2"

event_handler = FileHandler()
observer = observers.Observer()
observer.schedule(event_handler, home, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()