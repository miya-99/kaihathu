import tkinter as tk

# ウィンドウを作成
window = tk.Tk()
window.title("ボタンの例")

# ボタンを作成
button = tk.Button(window, text="クリックしてください")

# ボタンがクリックされたときに実行される関数
def button_click():
    button.config(text="クリックされました！")

button.config(command=button_click)

# ボタンをウィンドウに配置
button.pack()

# イベントループを開始
window.mainloop()
