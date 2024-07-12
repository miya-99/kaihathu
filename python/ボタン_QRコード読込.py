import cv2
import tkinter as tk
from tkinter import ttk
from pyzbar.pyzbar import decode
from PIL import Image
from PIL import ImageTk

# カメラキャプチャを初期化
cap = cv2.VideoCapture(0)

# カメラ映像を表示する関数
def show_frame():
    ret, frame = cap.read()
    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        panel.imgtk = imgtk
        panel.config(image=imgtk)
        panel.after(10, show_frame)

# QRコードを読み取る関数
def read_qr_code():
    ret, frame = cap.read()
    if ret:
        decoded_objects = decode(frame)
        if decoded_objects:
            qr_data = decoded_objects[0].data.decode('utf-8')
            result_label.config(text="QRコードデータ: " + qr_data)

# ウィンドウを作成
root = tk.Tk()
root.title("QRコードリーダー")

# 映像表示用のラベル
panel = ttk.Label(root)
panel.pack(padx=10, pady=10)
show_frame()

# ボタンを作成
button = ttk.Button(root, text="QRコードを読み取る", command=read_qr_code)
button.pack(padx=10, pady=10)

# QRコードデータを表示するラベル
result_label = ttk.Label(root, text="")
result_label.pack(padx=10, pady=10)

# ウィンドウを開始
root.mainloop()
