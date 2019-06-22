# create a gui
import tkinter as tk
import tkinter.filedialog
import instagram as ig
from PIL import Image
from io import BytesIO

# window
win = tk.Tk()
win.title("ig grab")
# win.configure(background='default')

# Frames
urlFrame = tk.Frame(win, pady="4", padx="4")
urlFrame.pack()

dirFrame = tk.Frame(win, pady="4", padx="4")
dirFrame.pack()
# input to grab URL
inputLabel = tk.Label(urlFrame, text="Enter IG URL:", anchor="w")
inputLabel.pack(fill="both")

inputField = tk.Entry(urlFrame)
inputField.pack(anchor="w")

# func that does grabbing
def grabInput(event):
    url = inputField.get()
    inputField.delete(0, tk.END )
    print(url)

# choose directory to save
dirEntry = tk.Entry(dirFrame)
def chooseDir(event="event"):
    # win.withdraw() # this hides the window
    selectedDir = tk.filedialog.askdirectory()
    dirEntry.delete(0, tk.END)
    dirEntry.insert(0, selectedDir)
dirLabel = tk.Label(dirFrame, text="Choose a location to save:")

dirMeatballs = tk.Button(dirFrame, text="...", command=chooseDir)
dirLabel.pack()
dirEntry.pack(side=tk.LEFT)
dirMeatballs.pack()

inputField.bind("<Return>", grabInput)

# close on Esc key
def quit(e):
    print(e)
    win.destroy()
win.bind("<Escape>", quit)
# add a preview

# add a save button
import requests
# see if grab url works
def grabUrl():
    url = inputField.get()
    imgArr = ig.grabUrl(url) # ig func
    # turn url into image data
    img = Image.open(BytesIO(imgArr[0].content))
    getDir = dirEntry.get()
    ext = imgArr[1]
    if ext == 'jpg':
        pilExt = 'JPEG'
    elif ext == 'png':
        pilExt = 'PNG'
    img.save(getDir + "/" + imgArr[2] + "." + ext, pilExt)

getUrlButton = tk.Button(master=win, text="Save", command=grabUrl)
getUrlButton.pack()

# event loop
win.mainloop()