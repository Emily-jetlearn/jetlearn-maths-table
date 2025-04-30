from tkinter import *
from tkinter.ttk import *
window=Tk()
window.title("Mathematical table")

caption=Label(window,text="Multiplication table generator")
caption.grid(row=0,column=0,columnspan=3)
range=Label(window, text="Range of numbers")
range.grid(row=1,column=2)
thenum=IntVar()
numbers=Combobox(window,textvariable=thenum,width=3)
numbers.grid(row=1,column=1)
numbers["values"]=tuple(range(101))

end_value=IntVar()
r10=Radiobutton(window,text="10",variable=end_value,value=10)
r10.grid(row=1,column=2)
r20=Radiobutton(window,text="20",variable=end_value,value=20)
r20.grid(row=2,column=2)
r30=Radiobutton(window,text="30",variable=end_value,value=30)
r30.grid(row=3,column=2)
end_value.set(10)

def tablegen():
    table=""
    for i in range (end_value.get +1):  
        table += str(thenum.get()) + " x " + str(i) + " = " + str(thenum.get()*i)
    table.configure(text=table)

genbutton=Button(window,text="Generate",command=tablegen)
genbutton.grid(row=4,column=1)
tables=Label(window,anchor="center")
tables.grid(row=5,column=1)

window.mainloop()


