# Importing necessary modules
import os
import shutil
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, psutil
process = psutil.Process(os.getpid())

# Intializing
output_stream = sys.stdout

# Path of folder to be sorted
f = open('path.txt','r')
path = r''.join(str(f.read()))
f.close()

# Listing directory
directory = os.listdir(path)

# Extracting all files present in directory
files = [x for x in directory]

# Json of all common extensions
jsonOBJ = [
    {
        'exe' : {
            'ext': ['exe', 'msi'],
            'name': 'Softwares'
        },
        'image' : {
            'ext': ['jpg', 'jpeg', 'png', 'gif', 'jfif', 'bmp',
         'tiff'],
            'name': 'Images'
        },
        'FILE' : {
            'ext': ['psd', 'eps', 'ai', 'raw', 'indd','aep','ipynb','py','css','js','php', 'xml','blend'],
            'name': 'Files'
        },
        'audio' : {
            'ext': ['mp3', 'mov', 'wav', 'pcm', 'aiff',
         'acc', 'ogg', 'wma', 'flac', 'alac', ''],
            'name': 'Audio'
        },
        'video' : {
            'ext': ['mp4', 'wmv', 'avi', 'avchd', 'flv',
         'f4v', 'swf', 'mkv', 'webm', 'mpeg-2'],
            'name': 'Videos'
        },
        'docs' : {
            'ext': ['esd', 'docx', 'pdf', 'txt', 'doc', 'html',
        'htm', 'odt', 'xls', 'xlsx', 'ods', 'ppt', 'pptx'],
            'name': 'Documents'
        },
        'archive' : {
            'ext': ['zip', 'tar', '7zip', 'rar', 'targz'],
            'name': 'Archives'
        },
    }
]

def checkForDir(fol, doc):
    # Checking for if directory is already present or not
    if not os.path.isdir(os.path.join(path, fol)):
        os.mkdir(os.path.join(path, fol))
        
    # Checking for if file is already present or not
    if os.path.isfile(os.path.join(path, doc)):
        shutil.move(os.path.join(path, doc),
                os.path.join(path, fol))

def sorting(files):
    # Getting each file in directory
    for file in files:
        # Splitting file names
        tmp = file.split('.')
        # Getting file extension for sorting process
        extension = tmp[1] if len(tmp) > 1 else tmp[0]
        # Iterating through JSON
        for i,j in jsonOBJ[0].items():
            # Getting all extension types
            for itm in j['ext']:
                # Checking for file types
                if extension in itm:
                    # Sending name of folder to be ceated and file in function
                    try:
                        checkForDir(j['name'], file)
                        # Displaying current file which is sorting
                        # output_stream.write('[DONE]:    %s\r' % file)
                        # output_stream.flush()
                        pass
                    except NameError:
                        output_stream.write('[ERROR]:    %s\r' % NameError)
                        output_stream.flush()
                
                    # For simplicity including time function
                    time.sleep(0.2)
                    
    # print('Sorting Done')



class Watcher:
    DIRECTORY_TO_WATCH = path

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        if event.event_type == 'modified':
            
            # Listing directory
            directory = os.listdir(path)

            # Extracting all files present in directory
            files = [x for x in directory]
            sorting(files)

if __name__ == '__main__':
    print('Sorting Files...')
    w = Watcher()
    w.run()