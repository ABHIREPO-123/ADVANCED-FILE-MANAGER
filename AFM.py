<<<<<<< HEAD
from tkinter import *
import os
import shutil

root = Tk()
root.title("ADVANCE FILE MANAGER")
root.geometry("1255x944")
root.wm_iconbitmap("AFM.ico")

def manageFiles():
    i=0
    dict = {
    'audio' : ('.mp3', '.m4a', '.wav', '.flac'),
    'video' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'document' : ('.docx', '.jpeg', '.jpg', '.pdf', '.txt', '.zip', '.bmp', '.pub', '.rar', '.pptx', '.accdb'),
    }
    output_content.insert(END, '################################################  BEFORE ARRANGE  ################################################# \n\n\n')
    path = folder_path.get()
    if os.path.exists('R:\\Arrange'):
        print('already')
    else:
        os.mkdir('R:\\Arrange')
    fileiter = os.walk(path)
    for current_path, folder_name, file_name in fileiter:
        print(f'current path : {current_path}')
        print(f'folder name : {folder_name}')
        print(f'file name : {file_name}')
        output_content.insert(END, 'current path: \t\t'+current_path+'\n\n')
        output_content.insert(END, 'folder name: \t\t'+str(folder_name)+'\n\n')
        output_content.insert(END, 'file name: \t\t'+str(file_name)+'\n\n\n\n')
        for file in file_name:
            for keys, values in dict.items():
                for i in range(len(values)):
                    if file.endswith(values[i]):
                        val = values[i].replace(".", "")
                        if os.path.exists('R:\\Arrange' + "\\" + val):
                            pass
                        else:
                            os.mkdir('R:\\Arrange' + "\\" + val)
                        shutil.copy(current_path + '\\' + file,'R:\\Arrange' + '\\' + val + '\\' + file)
    output_content.insert(END, '################################################  AFTER ARRANGE  ################################################# \n\n\n')
    fileiter = os.walk('R:\\Arrange')
    for current_path, folder_name, file_name in fileiter:
        print(f'current path : {current_path}')
        print(f'folder name : {folder_name}')
        print(f'file name : {file_name}')
        output_content.insert(END, 'current path: \t\t'+current_path+'\n\n')
        output_content.insert(END, 'folder name: \t\t'+str(folder_name)+'\n\n')
        output_content.insert(END, 'file name: \t\t'+str(file_name)+'\n\n\n\n')

heading = Label(root, text = "ADVANCE FILE MANAGER",bg ="#00008B", fg="white", padx=13, pady=10, font="comicsansms 20 bold", borderwidth=6, relief=RAISED )
heading.pack(side=TOP, fill=X, padx=0, pady=0)

f1 = Frame(root,bd=0, bg="#191970", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")


f2 = Frame(f1,bd=0, bg="#191970", borderwidth=0, relief=SUNKEN)
f2.pack(side=TOP, fill="none", pady=10)

about = Text(f2,height=9,width=52,font="comicsansms 14 bold ",bg="#191970",fg="white",padx=0,pady=0, borderwidth=0, relief=RIDGE)
about.pack(padx=2,pady=70)
about.insert(END,"You can easily manage your files by the use of this software.\n\nGive the path of the folder, who contains different types of files and folder.\n\nAfter click the start button this software append the same type of files in one folder(File type folder) and manage your files.")

l = Label(f2, text="Enter Folder Path",bg="#191970" , fg="white", padx=13, pady=8, font="comicsansms 20 bold", borderwidth=0, relief=RIDGE )
l.pack(padx=200, pady=10)

folder_path = StringVar()
enter_path = Entry(f2,textvariable = folder_path, bg="white" ,width=30, fg="black", font="comicsansms 20 bold", borderwidth=0, relief=RIDGE)
enter_path.pack(pady=10)
    
start = Button(f2,command=manageFiles, text="START",bg="#00008B" , fg="white", padx=6, pady=2, font="comicsansms 16 bold", borderwidth=2, relief=RIDGE )
start.pack(pady=20)


f3 = Frame(root, borderwidth=0, bg="white", relief=SUNKEN)
f3.pack(side=RIGHT, fill="y")

l = Label(f3, text="OUTPUT", font="Helvetica 12 bold",fg='black', bg="white", pady=6, width=100)
l.pack(side=TOP, pady=5)


scroll_x = Scrollbar(f3,orient=HORIZONTAL)
scroll_y = Scrollbar(f3,orient=VERTICAL)
output_content = Text(f3,font="comicsansms 10 ",padx=2,pady=8, borderwidth=0, relief=RIDGE, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x= Scrollbar(command=output_content.xview)
scroll_y= Scrollbar(command=output_content.yview)

output_content.pack(fill=BOTH,padx=15,pady=2 ,expand=1)

root.mainloop()
=======
from tkinter import *
import os
import shutil

root = Tk()
root.title("ADVANCE FILE MANAGER")
root.geometry("1255x944")
root.wm_iconbitmap("AFM.ico")

def manageFiles():
    i=0
    dict = {
    'audio' : ('.mp3', '.m4a', '.wav', '.flac'),
    'video' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'document' : ('.docx', '.jpeg', '.jpg', '.pdf', '.txt', '.zip', '.bmp', '.pub', '.rar', '.pptx', '.accdb'),
    }
    output_content.insert(END, '################################################  BEFORE ARRANGE  ################################################# \n\n\n')
    path = folder_path.get()
    if os.path.exists('R:\\Arrange'):
        print('already')
    else:
        os.mkdir('R:\\Arrange')
    fileiter = os.walk(path)
    for current_path, folder_name, file_name in fileiter:
        print(f'current path : {current_path}')
        print(f'folder name : {folder_name}')
        print(f'file name : {file_name}')
        output_content.insert(END, 'current path: \t\t'+current_path+'\n\n')
        output_content.insert(END, 'folder name: \t\t'+str(folder_name)+'\n\n')
        output_content.insert(END, 'file name: \t\t'+str(file_name)+'\n\n\n\n')
        for file in file_name:
            for keys, values in dict.items():
                for i in range(len(values)):
                    if file.endswith(values[i]):
                        val = values[i].replace(".", "")
                        if os.path.exists('R:\\Arrange' + "\\" + val):
                            pass
                        else:
                            os.mkdir('R:\\Arrange' + "\\" + val)
                        shutil.copy(current_path + '\\' + file,'R:\\Arrange' + '\\' + val + '\\' + file)
    output_content.insert(END, '################################################  AFTER ARRANGE  ################################################# \n\n\n')
    fileiter = os.walk('R:\\Arrange')
    for current_path, folder_name, file_name in fileiter:
        print(f'current path : {current_path}')
        print(f'folder name : {folder_name}')
        print(f'file name : {file_name}')
        output_content.insert(END, 'current path: \t\t'+current_path+'\n\n')
        output_content.insert(END, 'folder name: \t\t'+str(folder_name)+'\n\n')
        output_content.insert(END, 'file name: \t\t'+str(file_name)+'\n\n\n\n')

heading = Label(root, text = "ADVANCE FILE MANAGER",bg ="#00008B", fg="white", padx=13, pady=10, font="comicsansms 20 bold", borderwidth=6, relief=RAISED )
heading.pack(side=TOP, fill=X, padx=0, pady=0)

f1 = Frame(root,bd=0, bg="#191970", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")


f2 = Frame(f1,bd=0, bg="#191970", borderwidth=0, relief=SUNKEN)
f2.pack(side=TOP, fill="none", pady=10)

about = Text(f2,height=9,width=52,font="comicsansms 14 bold ",bg="#191970",fg="white",padx=0,pady=0, borderwidth=0, relief=RIDGE)
about.pack(padx=2,pady=70)
about.insert(END,"You can easily manage your files by the use of this software.\n\nGive the path of the folder, who contains different types of files and folder.\n\nAfter click the start button this software append the same type of files in one folder(File type folder) and manage your files.")

l = Label(f2, text="Enter Folder Path",bg="#191970" , fg="white", padx=13, pady=8, font="comicsansms 20 bold", borderwidth=0, relief=RIDGE )
l.pack(padx=200, pady=10)

folder_path = StringVar()
enter_path = Entry(f2,textvariable = folder_path, bg="white" ,width=30, fg="black", font="comicsansms 20 bold", borderwidth=0, relief=RIDGE)
enter_path.pack(pady=10)
    
start = Button(f2,command=manageFiles, text="START",bg="#00008B" , fg="white", padx=6, pady=2, font="comicsansms 16 bold", borderwidth=2, relief=RIDGE )
start.pack(pady=20)


f3 = Frame(root, borderwidth=0, bg="white", relief=SUNKEN)
f3.pack(side=RIGHT, fill="y")

l = Label(f3, text="OUTPUT", font="Helvetica 12 bold",fg='black', bg="white", pady=6, width=100)
l.pack(side=TOP, pady=5)


scroll_x = Scrollbar(f3,orient=HORIZONTAL)
scroll_y = Scrollbar(f3,orient=VERTICAL)
output_content = Text(f3,font="comicsansms 10 ",padx=2,pady=8, borderwidth=0, relief=RIDGE, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x= Scrollbar(command=output_content.xview)
scroll_y= Scrollbar(command=output_content.yview)

output_content.pack(fill=BOTH,padx=15,pady=2 ,expand=1)

root.mainloop()
>>>>>>> 8a928ae (working)
