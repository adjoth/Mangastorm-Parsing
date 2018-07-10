import os, tkinter

#Importing Classes
from mangaClass import Manga

##with open("favorites.msbf", "r") as f:
##    print(f.readline())

## SITES LISTING ##
# z03mangahere
# z10readmangatoday
# mangareader
# mangafoxmb     # Moblie Site
# mangafox       # Desktop Site
# z02batoto
# z13mangadex

allManga = []              # Empty Array

def main():
    top = tkinter.Tk()
    readTitles()
    #B = tkinter.Button(top, text = " Search ", command= search)
    #B.pack()
    
    menu()
    top.mainloop()
        

def search():
    title = input("Enter Title: ")
    title = title.lower()
    x = []
    for index, manga in enumerate(allManga):
        tem = manga.rtitle()
        tem = tem.lower()
        if(title in tem):
            #print(index)
            x.append(index)
    return(x)

def prTitles(x):
    for i in x:
        print(allManga[i].rtitle())

# Reading in values from text file
def readTitles():
    file = open("favorites.msbf", "r")          # Opens file (Remember to close when finished)
    dummy = file.readline()                     # Unknown Data
    for line in file:
        s, t, u, st, n = line.split('\t')
        allManga.append(Manga(s,t,u,st,n))
    file.close()

# Adding Title to list
def addTitle():
    print("1: Mangahere")
    print("2: Readmangatoday")
    print("3: Mangafox")
    print("4: Batoto")
    print("5: Mangadex")
    s = input("Site: ")
    if("s" == 1):
        s = "z03mangahere"
    if("s" == 2):
        s = "z10readmangatoday"
    if("s" == 3):
        s = "mangafoxmb"
    if("s" == 4):
        s = "z02batoto"
    if("s" == 5):
        s = "z13mangadex"
    t = input("Title: ")
    u = input("URL: ")
    st = input("Status: ")
    n = input("Num: ")
    newTitle = Manga(s,t,u,st,n)
    # How should I add to list [Append? Find it alphabetical location in list and insert?]
    # What does the number at the end mean?


def menu():
    print("Search")
    index = search()
    prTitles(index)
    

def clear():
    os.system("pause")
    os.system('cls' if os.name == 'nt' else 'clear')

main()
