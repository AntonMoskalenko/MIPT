import tkinter as tk

root = tk.Tk()  # Creation of main window/object

# Creation of objects inside the window
e = tk.Entry(root, width=20)
b = tk.Button(root, text='Convert')
l = tk.Label(root, bg='black', fg='white', width=20)


def strToSortList (event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)


b.bind('<Button-1>', strToSortList)  # Connecting action to function

# Putting widgets on the window one after one
e.pack()
b.pack()
l.pack()

root.mainloop()  # Opening window and waiting for the action



