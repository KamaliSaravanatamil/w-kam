from tkinter import Tk,ttk
from tkinter import *

from PIL import Image,ImageTk
#colors
cor0="#FFFFFF" #white
cor1="#333333" #black
cor2="#E85051" #red

window=Tk()
window.geometry('300x320')
window.title('Converter')
window.configure(bg=cor0)
window.resizable(height=FALSE,width=FALSE)

#frames
top=Frame(window,width=300,height=260,bg=cor0)
top.grid(row=0,column=0)

main=Frame(window,width=300,height=260,bg=cor0)
main.grid(row=1,column=0)

#top frame
icon=Image.open('C:\\Users\\Lenovo\\Downloads\\icons8-convert-64.png')
icon=icon.resize((40,40))
icon=ImageTk.PhotoImage(icon)
app_name=Label(top,image=icon,compound=LEFT,text="Currency Converter",height=5,padx=19,pady=30,anchor=CENTER,font=('Arial 16 bold'),bg=cor1,fg=cor0)
app_name.place(x=0,y=0)

#main frames
result=Label(main,text="",width=16,height=2,pady=7,relief="solid",anchor=CENTER,font=('Ivy 15 bold'),bg=cor2,fg=cor1)
result.place(x=50,y=10)
from_label =Label(main,text="From",width=8,height=1,pady=0,padx=0,relief="flat",anchor=NW,font=('Ivy 10 bold'),bg=cor0,fg=cor1)
from_label.place(x=48,y=90)

                           


                                                                                                                                    
window.mainloop()
