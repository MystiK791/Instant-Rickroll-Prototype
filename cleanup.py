import os

def cleanup(path, file):
    if os.path.exists(path):
        os.remove(path + '/' + file)
        os.rmdir(path)
