from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import moviepy.editor as me

filename=''

def convert():
        global filename
        filetypes=(("Audio files","*.mp3 , *.waw , *.ogg"),("All files","*.*"))
        video=me.VideoFileClip(filename)
        audio=video.audio
        file=asksaveasfilename(filetypes=filetypes)
        audio.write_audiofile(f'{file}{format.get()}')
        label5=Label(root,text="Finished",font=("Arial",15,"bold"),fg="green",bg="#232323")
        label5.pack()
        label5.place(x=450,y=300)
def select():
    global filename
    filetypes = (
        ('video files', '*.WEBM , *.MPEG , *.MPE , *.MKV , *.MP4 , *.M4P , *.M4V , *.AVI , *.WMV , *.MOV , *.FLV , *.AVCHD'),
        ('All files', '*.*')
    )
    filename=askopenfilename(filetypes=filetypes)
    label3.config(text="File Selected",fg="green",bg="#232323",font=("Arial",18))
    label4=Label(root,text="Select Audio format ",font=("Arial",18),bg="#232323",fg="white")
    label4.pack()
    label4.place(x=125,y=250)
    options=[".mp3",".ogg",".wav"]
    format.set(".mp3")
    menu=OptionMenu(root,format,*options)
    menu.pack()
    menu.config(bg="#808080",fg="black",font=("Arial",14))
    menu.place(x=355,y=250)
    button3=Button(root,text="Export",font=("Arial",12,"bold"),bg="#232323",fg="white",command=convert,width=10,height=1)
    button3.pack()
    button3.place(x=250,y=300)

root=Tk()
root.geometry("600x350")
root.minsize(600,350)
root.config(bg="#232323")
root.title("Video to Audio ")
# 0AK80
label1=Label(root,text="Video to Audio",font=("Arial",32,"bold"),bg="#232323",fg="white")
label1.pack()
label2=Label(root,text="Select Video to Convert",font=("Arial",18),bg="#232323",fg="white")
label2.pack()
label2.place(x=175,y=100)
button1=Button(root,text="Select",font=("Arial",12,"bold"),bg="#232323",fg="white",command=select,width=10,height=1)
button1.pack()
button1.place(x=250,y=200)
label3=Label(root,font=("Arial",18,"bold"))
label3.pack()
label3.place(x=225,y=150)
format=StringVar()


root.mainloop()
