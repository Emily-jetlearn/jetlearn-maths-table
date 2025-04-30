from tkinter import *
from tkinter.filedialog import *
window=Tk()
window.title("memoriser")

savebutton=Button(window,text="SAVE")
savebutton.pack(padx=30,pady=30)
openbutton=Button(window,text="OPEN")
openbutton.pack(padx=30,pady=30)
delbutton=Button(window,text="DELETE")
delbutton.pack(padx=30,pady=30)
addbutton=Button(window,text="ADD")
addbutton.pack(padx=30,pady=30)
listadd=Entry(window,width=40)
listadd.grid(row=1,column=1,padx=30,pady=30,columnspan=2)
f=Frame(window)
f.pack(side=RIGHT)
scroll=Scrollbar(f,orient="vertical")
scroll.pack(side=RIGHT,fill=Y)
memorise=Listbox(f,width=50,yscrollcommand=scroll.set,bg="#60b2bd")
memorise.pack(side=LEFT,padx=5,pady=5)
for i in range(1,1001):
    memorise.insert(END,"memory " + str(i))

scroll.config(command=memorise.yview)
window.mainloop()