import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win64':
    base = "Win64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Python\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python\tcl\tk8.6"

executables = [cx_Freeze.Executable("textEditor.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
