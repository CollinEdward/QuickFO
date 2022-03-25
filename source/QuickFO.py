# get current ip with api
# https://api.ipify.org
from tkinter import *
import os
import platform

# get local computer information with module platform and store the result in variable

# put all variables in string format

platform_version = platform.version()
platform_system = platform.system()
platform_machine = platform.machine()
platform_processor = platform.processor()
platform_python_version = platform.python_version()
platform_python_compiler = platform.python_compiler()
platform_python_build = platform.python_build()
platform_python_branch = platform.python_branch()
platform_python_implementation = platform.python_implementation()
platform_python_revision = platform.python_revision()
platform_python_version_tuple = platform.python_version_tuple()



api = "curl -s https://api.ipify.org"
ip = os.popen(api).read()

FOREGROUND = "#2c3e50" # color of text in window 
BACKGROUND = "#6a89cc" # color of background in window 

root = Tk()
root.title("IP")
root.geometry("500x350")
root.resizable(0,0)
root.configure(background=BACKGROUND)

# Make a label widget to display the IP address of the current computer in the GUI window 
# (use the api to get the IP address)
Label_current_ip = Label(root, text="\nCurrent IP: " + ip, background=BACKGROUND, foreground=FOREGROUND).pack()

label_computer_info = Label(root, text="\nComputer Information: ", background=BACKGROUND, foreground=FOREGROUND).pack()
information_label = Label(root, background=BACKGROUND, foreground=FOREGROUND, text="\nPlatform: " + str(platform_system) + "\nVersion: " + str(platform_version) + "\nMachine: " + str(platform_machine) + "\nProcessor: " + str(platform_processor) + "\nPython Version: " + str(platform_python_version) + "\nPython Compiler: " + str(platform_python_compiler) + "\nPython Build: " + str(platform_python_build) + "\nPython Branch: " + str(platform_python_branch) + "\nPython Implementation: " + str(platform_python_implementation) + "\nPython Revision: " + str(platform_python_revision) + "\nPython Version Tuple: " + str(platform_python_version_tuple)).pack()

Label_space = Label(root, text="\n", background=BACKGROUND).pack()

button_exit = Button(root, text="EXIT", background=FOREGROUND, foreground=BACKGROUND, command=root.destroy, border=0, borderwidth=0, width=13, height=2).pack()

root.mainloop()