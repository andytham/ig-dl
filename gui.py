# create a gui
import tkinter as tk
import tkinter.filedialog
import instagram as ig
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

#TODO add a preview

# Grab and saves image
def saveUrl():
    url = inputField.get()
    res = ig.scrapeUrl(url) # ig func
    '''
    structure of res
    {
        "filename": filename,
        "fileList": [
            [requests.get(url), ext],
            ...
        ]
    }
    '''

    for index, file in enumerate(res["fileList"]):
        directory = dirEntry.get()
        filename = res["filename"]
        fileData = file[0].content
        ext = file[1]
        if len(res["fileList"]) == 1: # if there's only one item
            open(f"{directory}/{filename}.{ext}", 'wb').write(fileData)
        else:
            open(f"{directory}/{filename} {index}.{ext}", 'wb').write(fileData)
        index += 1

getUrlButton = tk.Button(master=win, text="Save", command=saveUrl)
getUrlButton.pack()

# event loop
win.mainloop()