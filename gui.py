
# create a gui
import tkinter as tk
import tkinter.filedialog

# window
win = tk.Tk()
win.title("ig grab")

# input to grab URL
inputLabel = tk.Label(win, text="Enter IG URL:")
inputLabel.pack()

inputField = tk.Entry(win)
inputField.pack()

def chooseDir():
    # win.withdraw()
    selectedDir = tk.filedialog.askdirectory()
    print(selectedDir)
dirButton = tk.Button(win, text="Choose location to save:", command=chooseDir)
dirButton.pack()

# func that does grabbing
def grabInput(event):
    url = inputField.get()
    inputField.delete(0, tk.END )
    print(url)



inputField.bind('<Return>', grabInput)


# event loop
win.mainloop()