from tkinter import *

window=Tk()
window.title("CALCULATOR")
window.configure(bg="black")
window.geometry( '400x600' )
label=Label(window,text=" ",bg="black")
label.pack()


def click(event):

     text=event.widget.cget("text")
     print(text)
     if text=="=":
         if scvalue.get().isdigit():
             value=int(scvalue.get())
         else :
             value=eval(screen.get())
         scvalue.set(value)
         screen.update()

     elif text=="CLR":
         scvalue.set(" ")
         screen.update()
     else:
         scvalue.set(scvalue.get()+text)
         screen.update()




scvalue=StringVar()
scvalue.set("")
screen=Entry(window,width="40",textvar=scvalue,bd=45,insertwidth=5,font=10,bg='#088A85')

screen.pack(side=TOP)
label=Label(window,text=" ",bg="black")
label.pack()


frame=Frame(window,bg="black")
b=Button(frame,padx=15,pady=16,bd=20,text="9",bg='#088A85',font=15)
b.pack(side=LEFT)

b.bind("<Button-1>",click)
b=Button(frame,padx=16,pady=16,bd=20,text="8",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(frame,padx=16,pady=16,bd=20,text="7",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,padx=16,pady=16,bd=20,text="+",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

frame.pack(side=TOP)


frame=Frame(window)
b=Button(frame,padx=16,pady=16,bd=20,text="6",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,padx=16,pady=16,bd=20,text="5",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(frame,padx=16,pady=16,bd=20,text="4",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,padx=16,pady=16,bd=20,text="-",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)


frame.pack(side=TOP)



frame=Frame(window)
b=Button(frame,padx=16,pady=16,bd=20,text="3",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,padx=16,pady=16,bd=20,text="2",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(frame,padx=16,pady=16,bd=20,text="1",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,padx=16,pady=16,bd=20,text="/",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

frame.pack(side=TOP)



frame=Frame(window)
b=Button(frame,padx=18,pady=16,bd=20,text="0",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,padx=16,pady=16,bd=20,text=".",bg='#088A85',font=100)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(frame,padx=16,pady=16,bd=20,text="=",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,padx=16,pady=16,bd=20,text="*",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

frame.pack(side=TOP)


frame=Frame(window)



b=Button(frame,padx=16,pady=16,bd=30,text="%",bg='#088A85',font=15)
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,padx=65,pady=16,bd=30,text="CLR",bg='#B40404',font=35)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

frame.pack(side=TOP)

window.mainloop()#window never close
