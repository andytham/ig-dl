# create a gui
import tkinter as tk

# window
win = tk.Tk()
win.title("ig grab")

# input to grab URL
inputLabel = tk.Label(win, text="test")
inputLabel.pack()

inputField = tk.Entry(win)
inputField.pack()

# func that does grabbing
def grabInput(event):
    url = inputField.get()
    inputField.delete(0, tk.END )
    print(url)

inputField.bind('<Return>', grabInput)


# event loop
win.mainloop()