from pygame import Color, mixer
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os

class mymusicplayer:
    def __init__(self,window):
        window.geometry('1000x500')
        window.title("Music Player")
        window.resizable(0, 0)
        
        self.playvar=tk.StringVar()
        self.pausevar=tk.StringVar()
        self.playvar.set('Play')
        self.pausevar.set('Pause')
        
        self.currentlyplaying=False
        self.loadedfile=False
        self.loadedfilename=tk.StringVar()
        self.loadedfilename.set('None')
        self.currvol=tk.StringVar()
        self.currvol.set('0')
        self.currvolvar=1.00

        openBtn=Button(window, text="Open", width = 20, font = ('Comic Sans MS',20),command=self.open,bg='#D6A9D5')
        openBtn.place(x=250,y=100,anchor='center')
        playBtn=Button(window, textvariable=self.playvar, width = 20, font = ('Comic Sans MS',20),command=self.play,bg='#D6A9D5')
        playBtn.place(x=250,y=200,anchor='center')
        pauseBtn=Button(window, textvariable=self.pausevar, width = 20, font = ('Comic Sans MS',20),command=self.pause,bg='#D6A9D5')
        pauseBtn.place(x=250,y=300,anchor='center')
        exitBtn=Button(window, text="Stop", width = 20, font = ('Comic Sans MS',20),command=self.exit,bg='#D6A9D5')
        exitBtn.place(x=250,y=400,anchor='center')
        VolIncrBtn=Button(window,text="➕",width = 4, font= ('Comic Sans MS',10),bg='black',fg='#D6A9D5',command=self.volincr )
        VolIncrBtn.place(x=690,y=400,anchor='center')
        VolDcrBtn=Button(window,text="➖",width = 4, font= ('Comic Sans MS',10),bg='black',fg='#D6A9D5',command=self.voldcr )
        VolDcrBtn.place(x=810,y=400,anchor='center')

        
        logo=tk.Label(window,width=10,text="Music 🎧",font=('Monaco',50),bg='black',fg='#B3F5FF')#image=logoimg)
        logo.place(x=575,y=100) 
        playing=tk.Label(window,width=20,text="Current Tune 🎵",font=('Trattatello',20),bg='black',fg='#E1C7E0')#image=logoimg)
        playing.place(x=600,y=200) 
        currentplaying=tk.Label(window,width=50,textvariable=self.loadedfilename,font=('Trattatello',12),bg='black',fg='#C054BE')
        currentplaying.place(x=525,y=250)
        vollabel=tk.Label(window,width=10,text="Volume 🔊",font=('Trattatello',20),bg='black',fg='#E1C7E0')#image=logoimg)
        vollabel.place(x=675,y=300)
        currentvol=tk.Label(window,width=50,textvariable=self.currvol,font=('Trattatello',12),bg='black',fg='#C054BE')
        currentvol.place(x=525,y=350)
        

    def open(self):
        if self.loadedfile and (not self.currentlyplaying):
            mixer.music.pause()
            self.pausevar.set('Resume')
        self.loadedfile= filedialog.askopenfilename()
        #self.loadedfilename.set(self.loadedfile)
        self.name=os.path.basename(self.loadedfile)
        self.playvar.set('Play')
        self.loadedfilename.set(self.name)

    def play(self):
        if self.loadedfile:
            mixer.init()
            mixer.music.load(self.loadedfile)
            mixer.music.play()
            self.currentlyplaying=False
            self.pausevar.set('Pause')
            self.playvar.set('Restart')
            mixer.music.set_volume(self.currvolvar)
            self.currvol.set(100*self.currvolvar)


    def pause(self):
        if not self.currentlyplaying:
            mixer.music.pause()
            self.currentlyplaying=True
            self.pausevar.set('Resume')
        else:
            mixer.music.unpause()
            self.currentlyplaying=False  
            self.pausevar.set('Pause')   

    def exit(self):
        mixer.music.stop()
        self.playvar.set('Play')
        self.pausevar.set('Pause')  
        

    def volincr(self):
        if self.currvolvar<1:    
            self.currvolvar+=0.05
            self.currvolvar = round(self.currvolvar,2)
            mixer.music.set_volume(self.currvolvar)
            self.currvol.set(int(100*self.currvolvar))

    def voldcr(self):
        if self.currvolvar>0:
            self.currvolvar-=0.05
            self.currvolvar = round(self.currvolvar,2)
            mixer.music.set_volume(self.currvolvar)
            self.currvol.set(int(100*self.currvolvar))





root = Tk()
root.configure(bg='black')
mymusicplayer(root)
root.mainloop()