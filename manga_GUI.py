import os, tkinter
from tkinter import ttk, messagebox, Listbox, Scrollbar, Radiobutton

#Importing User Classes
from mangaClass import Manga as MangaTitles

## SITES LISTING ##
# z03mangahere
# z10readmangatoday
# mangareader
# mangafoxmb     # Moblie Site
# mangafox       # Desktop Site
# z02batoto
# z13mangadex

allManga = []

class Manga(ttk.Frame):
    """The gui and functions."""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def on_quit(self):
        """Exits program."""
        quit()
        
    def search(self):
        #print("Inside Search")  # Debuging
        title = self.name.get()
        title = title.lower()
        x = []
        for index, manga in enumerate(allManga):
            tem = manga.rtitle()
            tem = tem.lower()
            if(title in tem):
                #print(index)
                x.append(index)
        self.printTitles(x)
        #print("Exiting Search") # Debuging


    def printTitles(self, x):
        #print("Inside Print Titles")    # Debuging
        #os.system("cls")    # Clears Screen
        self.Lb1.delete(0, tkinter.END)
        for i in x:
            self.Lb1.insert(i, allManga[i].rtitle())
            #print(allManga[i].rtitle())
        #print("Exiting Print Titles")   # Debuging

    def readTitles(self):
        file = open("favorites.msbf", "r")          # Opens file (Remember to close when finished)
        dummy = file.readline()                     # Unknown Data
        for line in file:
            s, t, u, st, n = line.split('\t')
            allManga.append(MangaTitles(s,t,u,st,n))
        file.close()

    def init_gui(self):
        """Builds GUI"""
        self.readTitles()
        
        self.root.title("Manga Storm")
        self.root.option_add('*tearOff', 'FALSE')
 
        self.grid(column=0, row=0, sticky='nsew')
 
        self.menubar = tkinter.Menu(self.root)

        # Menu Exit
        self.menu_file = tkinter.Menu(self.menubar)
        self.menu_file.add_command(label='Exit', command=self.on_quit)

        # Menu Edit
        self.menu_edit = tkinter.Menu(self.menubar)

        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit')

        self.root.config(menu=self.menubar)

        self.name = ttk.Entry(self, width=20)
        self.name.grid(column=1, row = 1)

        self.search_button = ttk.Button(self, text="Search", command = self.search)
        self.search_button.grid(column=2, row=1, columnspan=3)

        # Radio Buttons
        MODES = [
            ("Mangahere", "z03mangahere"),
            ("Readmangatoday","z10readmangatoday"),
            ("Mangareader","mangareader"),
            ("Mangafox","mangafoxmb"),
            ("Batoto","z02batoto"),
            ("Mangadex","z13mangadex")
            ]
        v = tkinter.StringVar()
        v.set("L")  # initialize
        for text, mode in MODES:
            b = Radiobutton(self, text = text, variable = v, value = mode)
            b.grid(column=1,row=2, sticky = tkinter.W)          # Needs to place radio buttons side by side

        # Scrollbar for listbox
        #self.scrollbar = Scrollbar(self)
        #self.scrollbar.grid(column = 1, row = 6)
        
        self.Lb1 = Listbox(self, width = 80, height = 20)   # yscrollcommand = self.scrollbar.set
        self.Lb1.grid(column=1, row = 5, columnspan=2)
        #items = self.Lb1.curselectoin

        #Scrollbar for listbox config
        #self.scrollbar.config(command=Lb1.yview)  #Lb1 not found
        
        ttk.Separator(self, orient='horizontal').grid(column=0,
                row=3, columnspan=4, sticky='ew')

        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

            
if __name__=="__main__":
    root = tkinter.Tk()
    root.geometry("500x500+200+200") 
    Manga(root)
    root.mainloop()
