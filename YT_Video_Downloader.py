#Import Libraries
from tkinter import *
from pytube import YouTube

#Create Display Window
root = Tk()
root.geometry('700x290')
root.resizable(0,0)
root.title("Aman: YouTube Video Downloader")

Label(root,text = 'Youtube Video Downloader', font ='Consolas 22 bold').pack()


#Create Field to Enter Link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'Consolas 11 bold').place(x= 32 , y = 70)
link_enter = Entry(root, width = 80,textvariable = link).place(x = 32, y = 100)


#Create Function to Start Downloading
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'Successfully Downloaded', font = 'Calibri 12', fg = 'green').place(x= 230 , y = 140)  

Button(root,text = 'DOWNLOAD', font = 'Corbel 15 bold' ,bg = 'yellow green', padx = 2, command = Downloader).place(x=250 ,y = 200)

root.mainloop()


