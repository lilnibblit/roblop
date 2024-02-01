from tkinter.filedialog import askopenfilename
path = askopenfilename(title="Select the Path", filetypes=(("Executable files", "*.exe"), ("All Files", "*.*")))

with open(path, "rb") as gd:
    gdr = gd.read()
    if gdr.find(b'\xe8\xc7\x1d\xc9\xff\x84\xc0\xeb\x1c') != -1:
        print("already")
        input()
        exit()
    
    rpl = gdr.replace(b'\xe8\xc7\x1d\xc9\xff\x84\xc0\x75\x1c', b'\xe8\xc7\x1d\xc9\xff\x84\xc0\xeb\x1c')

    if rpl.find(b'\xe8\xc7\x1d\xc9\xff\x84\xc0\xeb\x1c') != -1:
        print("success")
    else:
        print("ur not lucky")
        input()
        exit()

with open(path, "wb") as gdw:
    gdw.write(rpl)
