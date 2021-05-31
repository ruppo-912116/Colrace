import os
import cx_Freeze
os.environ['TCL_LIBRARY'] ="C:\\Users\Rupan\AppData\Local\Programs\Python\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] ="C:\\Users\Rupan\AppData\Local\Programs\Python\Python36-32\\tcl\\tk8.6"


executables = [cx_Freeze.Executable("pygame intro.py")]

cx_Freeze.setup(
    name = "Colrace",
    options= {"build_exe":{"packages":["pygame"],"include_files":["bus1.png","busicon.png","zero.mp3","crash.wav"]}},
    description = "Race against time",
    executables = executables
)
