from cx_Freeze import setup, Executable

setup(name='Lernspiel',version='1.0',description='Ein Lernspiel',executables = [Executable("index.py")])