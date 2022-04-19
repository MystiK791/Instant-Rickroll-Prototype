
#Import the built-in libraries that don't need to be installed
import os, cleanup
from zipfile import ZipFile

#Attempt to import the required libraries, and install them if not found
try:
    from moviepy.editor import *
    import pygame
except ImportError:
    os.system('py3 -m pip install wheel')
    os.system('py3 -m pip install pygame')
    os.system('py3 -m pip install moviepy')

#Function to extract the given Zip File (fileName) to the given directory (path)
def extractMovie(fileName, path):
    print("Setting up...")
    if not os.path.exists(path + '\rickroll.mp4'):
        with ZipFile(fileName, 'r') as zip:
            zip.extractall(path)

#Function to setup and load the mp4 at pathToFile
def setupClip(pathToFile):
    pygame.init()

    pygame.display.set_caption('You Got Rickrolled!')

    video = VideoFileClip(pathToFile)

    return video

#Main function
def main():
    extractMovie('data.zip', 'data')
    video = setupClip('data/rickroll.mp4')
    video.preview()

    pygame.quit()

    video.close()

    cleanup.cleanup('data','rickroll.mp4')

#Run the program if the namespace __name__ is __main__
if __name__ == "__main__":
    main()
