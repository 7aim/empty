from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

master = Tk()
master.title("Title")


canvas = Canvas(master,height=500,width=500) #create canvas
# pack place grid
canvas.pack() #run the canvas

frame = Frame(master,bg="#c1c1c1") #create a frame
frame.place(relx=0,rely=0,relheight=1,relwidth=1) #run the frame

label = Label(frame,text="TEXT",bg="#efefe8",font="Verdana 12 bold")
label.pack(padx=10,pady=10,side=LEFT) #pad = collider


#option menu
dropdown_default = StringVar(frame) #create default string
dropdown_default.set("DEFAULT")

dropdown = OptionMenu(frame,dropdown_default,"Menu 1","Menu 2") #create optionmenu
dropdown.pack(padx=10,pady=10,side=LEFT)


#date menu
datemenu_secici = DateEntry(
    frame,
    background="blue",          
    foreground="pink", #text color
    borderwidth=2, 
    headersbackground="red", #title color
    headersforeground="black" #title text color
)

datemenu_secici._top_cal.overrideredirect(True)
datemenu_secici.pack(padx=10,pady=10,side=LEFT)


#radio button
var =IntVar(frame)

radiobutton1 = Radiobutton(frame,text="Button1",variable=var,value=1,bg="#efefe8",font="Verdana 8")
radiobutton1.pack(anchor=NW,padx=0,pady=10)

radiobutton2 = Radiobutton(frame,text="Button2",variable=var,value=2,bg="#efefe8",font="Verdana 8")
radiobutton2.pack(anchor=NW,padx=0,pady=10)

radiobutton3 = Radiobutton(frame,text="Button3",variable=var,value=3,bg="#efefe8",font="Verdana 8")
radiobutton3.pack(anchor=NW,padx=0,pady=10)


#check button
var1 =IntVar(frame)
checkbutton1 = Checkbutton(frame,text="Button1",variable=var1,bg="#efefe8",font="Verdana 8")
checkbutton1.pack(anchor=NW,padx=0,pady=10)

var2 =IntVar(frame)
checkbutton2 = Checkbutton(frame,text="Button2",variable=var2,bg="#efefe8",font="Verdana 8")
checkbutton2.pack(anchor=NW,padx=0,pady=10)

var3 =IntVar(frame)
checkbutton3 = Checkbutton(frame,text="Button3",variable=var3,bg="#efefe8",font="Verdana 8")
checkbutton3.pack(anchor=NW,padx=0,pady=10)


#text area
text_area = Text(frame,height=10,width=30)
text_area.tag_configure("style",foreground='#bfbfbf',font=("Verdana",7,"bold"))
text_area.pack()
welcome_text="Metin giriniz..."
text_area.insert(END,welcome_text,"style",)


#buton and function
def gonder():
    print(text_area.get("1.0", "end-1c"))
    if var.get() == 1:
        messagebox.showinfo("Baslik","Buton1 e basildi")
    

send_button = Button(frame,text="Buton1",command=gonder)
send_button.pack()


master.mainloop() #keeps the window open
#master.destroy()