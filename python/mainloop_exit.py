import tkinter as tk
root = tk.Tk()
root.title("tkinterによるGUI画面作成")
root.geometry("300x100")

button = tk.Button(root, text="Exit", command=lambda:root.destroy())
button.pack()

root.mainloop()
