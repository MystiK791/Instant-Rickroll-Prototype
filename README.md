# Instant Rickroll Prototype
A prototype of a Python-based Rickroll program.

## Disclaimer
This repo DOES include a .mp4 of the official "Never Gonna Give You Up" music video (source: https://www.youtube.com/watch?v=dQw4w9WgXcQ). If Rick Astley or his record label has a problem with this, I will remove the video from the repo and rewrite the instructions to include obtaining and zipping your own copy.

## Functionality
The program comes bundled with two Python files, "main.py" and "cleanup.py". Running main.py will do the following
1. It will open a Python terminal that prints "Setting up...". In the background, the program will extract data.zip to a folder called "data" in the working directory. It will also check for Pygame and Moviepy and install them if not found.
2. The program will open a Pygame window that plays "Never Gonna Give You Up"
3. After the Pygame window is closed, "cleanup.py" will execute and attempt to delete the "data" folder. 

## Usage
1. Install Python from python.org if you haven't already (note: it's **CRUCIAL** that you tick the "Add Python to PATH" box during installation, otherwise when the program attempts to install Moviepy, it will fail)
2. Trick someone into running "main.py"
3. Sit back and watch the fireworks
