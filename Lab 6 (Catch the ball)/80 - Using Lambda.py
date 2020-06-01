import tkinter as tk

def main():
    WIDTH = 200
    root = tk.Tk()
    pl_canvas = tk.Canvas(root, width=WIDTH, height=200, bg='white')

    q_label = tk.Label(root, fg='black', width=20, text='Please enter your name:')
    data_entry = tk.Entry(root, width=20)
    save_button = tk.Button(root, text='Save', command=lambda: save_button_click(root, data_entry))

    q_label.pack()
    data_entry.pack()
    save_button.pack()

    pl_canvas.pack()
    root.mainloop()


def save_button_click(root, data_entry):
    player = data_entry.get()
    print(player)
    root.destroy()

if __name__ == "__main__":
    main()

