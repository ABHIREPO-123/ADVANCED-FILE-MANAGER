<<<<<<< HEAD
import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\abhishek\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\abhishek\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("AFM.py", base=base, icon="AFM.ico")]


cx_Freeze.setup(
    name = "ADVANCE FILE MANAGER",
    options = {"build_exe": {"packages":["tkinter","os","shutil"], "include_files":["AFM.ico",'tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
=======
import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\abhishek\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\abhishek\AppData\Local\Programs\Python\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("AFM.py", base=base, icon="AFM.ico")]


cx_Freeze.setup(
    name = "ADVANCE FILE MANAGER",
    options = {"build_exe": {"packages":["tkinter","os","shutil"], "include_files":["AFM.ico",'tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
>>>>>>> 8a928ae (working)
