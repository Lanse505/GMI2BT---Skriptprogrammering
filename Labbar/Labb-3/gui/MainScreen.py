from tkinter import *


def onUnfocus(event, search_input):
    if event.widget == search_input:
        pass



def renderMainScreen():
    root = Tk()
    root.configure(width=1080, height=720)
    label = Label(root, text="OMDB API Searcher")
    label.place(relx=0.5, anchor="n")

    searchInput = Text(root, width=75, height=1)
    searchInput.place(relx=0.5, y=100, anchor="center")
    searchInput.bind("<FocusOut>", onUnfocus)

    textOutput = Text(root, width=75, height=30)
    textOutput.place(relx=0.5, y=375, anchor="center")
    textOutput.config(state="disabled")

    root.mainloop()






