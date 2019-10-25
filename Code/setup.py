#File used to "freeze" executable file for the currently crunning OS.
#Currently there are builds for Win64 & Win32 premade

from cx_Freeze import setup, Executable

setup(name='Lernspiel',version='1.0',description='Ein Lernspiel',executables = [Executable("index.py")])