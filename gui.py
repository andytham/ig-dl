# create a gui
import tkinter as tk
import tkinter.filedialog
import instagram as ig
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

# see if grab url works
def testFunc():
    print("test func running")
    url = inputField.get()
    imgUrl = ig.grabUrl(url)
    print(imgUrl)

getUrlButton = tk.Button(master=win, text="Save", command=testFunc)
getUrlButton.pack()

# event loop
win.mainloop()