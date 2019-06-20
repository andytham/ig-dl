# create a gui
import tkinter as tk
import tkinter.filedialog
import instagram as ig
from PIL import Image
from io import BytesIO

# window
win = tk.Tk()
win.title("ig grab")

# input to grab URL
inputLabel = tk.Label(win, text="Enter IG URL:")
inputLabel.pack()

inputField = tk.Entry(win)
inputField.pack()

# func that does grabbing
def grabInput(event):
    url = inputField.get()
    inputField.delete(0, tk.END )
    print(url)

# choose directory to save
dirEntry = tk.Entry(win)
def chooseDir(event="event"):
    # win.withdraw() # this hides the window
    selectedDir = tk.filedialog.askdirectory()
    dirEntry.delete(0, tk.END)
    dirEntry.insert(0, selectedDir)
dirButton = tk.Button(win, text="Choose location to save:", command=chooseDir)
dirButton.pack()
dirEntry.pack()

dirEntry.bind('<Button-1>', chooseDir) # click on entry field
inputField.bind('<Return>', grabInput)


# add a preview

# add a save button
import requests
# see if grab url works
def grabUrl():
    url = inputField.get()
    imgRes = ig.grabUrl(url) # ig func
    img = Image.open(BytesIO(imgRes.content))
    img.show()

getUrlButton = tk.Button(master=win, text="Save", command=grabUrl)
getUrlButton.pack()

# event loop
win.mainloop()