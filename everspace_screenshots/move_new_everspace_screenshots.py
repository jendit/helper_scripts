from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import shutil
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            print(filename)
            src = os.path.join(folder_to_track, filename)
            new_desintation = os.path.join(folder_destination, filename)
            # shutil.copyfile(src, new_desintation)
            shutil.copy2(src, new_desintation)


folder_to_track = r"C:\Users\Dittmar\AppData\Local\RSG\Saved\Screenshots\WindowsNoEditor"
folder_destination = r"F:\Google Drive\Games\Everspace"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
