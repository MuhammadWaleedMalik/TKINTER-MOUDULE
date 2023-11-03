from tkinter import *
def Onclick():
    mil=int(miles.get())
    km=0
    km=float(mil)*1.609
    kilo.insert(END,f"{km}")

    
window=Tk()
window.minsize(500,500)
window.title("Miles TO Kilo Meter")


miles=Entry()
miles.insert(END,"0")
miles.place(x=200,y=200)

head=Label(text="MILES TO KILOMETER",fg="GREEN")
head.place(x=200,y=100)

label1=Label(text="Miles")
label1.place(x=320,y=200)
label2=Label(text="is Equal to")
label2.place(x=100,y=220)
kilo=Entry()
kilo.place(x=200,y=220)
label3=Label(text="kiloMeters")
label3.place(x=320,y=220)

button=Button(text="Calculate",command=Onclick)
button.place(x=320,y=240)











window.mainloop()