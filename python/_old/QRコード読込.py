import cv2
import tkinter as tk
from tkinter import ttk
from pyzbar.pyzbar import decode
from PIL import Image
from PIL import ImageTk

# カメラキャプチャを初期化
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200) # カメラ画像の横幅を1280に設定
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200) # カメラ画像の縦幅を720に設定

font = cv2.FONT_HERSHEY_SIMPLEX

# カメラ映像を表示する関数
def show_frame():
    ret, frame = cap.read()
    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        show_QR_frame(cv2image)
#        decoded_objects = decode(cv2image)
#        if decoded_objects:
#            qr_data = decoded_objects[0].data.decode('utf-8')
#            font_color = (0, 154, 87)
#            x, y, w, h = decoded_objects[0].rect
#            cv2.rectangle(cv2image, (x, y), (x + w, y + h), font_color, 2)
#            cv2image = cv2.putText(cv2image, qr_data, (x, y - 10), 
#                             font, .5, font_color, 2, cv2.LINE_AA)
            #cv2.imshow('BARCODE READER', cv2image)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        panel.imgtk = imgtk
        panel.config(image=imgtk)
        panel.after(10, show_frame)
        
# バーコードの枠を作成する関数
def show_QR_frame(fr):
    decoded_objects = decode(fr)
    if decoded_objects:
        qr_data = decoded_objects[0].data.decode('utf-8')
        font_color = (0, 154, 87)
        x, y, w, h = decoded_objects[0].rect
        cv2.rectangle(fr, (x, y), (x + w, y + h), font_color, 2)
        fr = cv2.putText(fr, qr_data, (x, y - 10), 
                            font, .5, font_color, 2, cv2.LINE_AA)
        #cv2.imshow('BARCODE READER', fr)
        
# QRコードを読み取る関数
def read_qr_code():
    ret, frame = cap.read()
    if ret:
        decoded_objects = decode(frame)
        if decoded_objects:
            qr_data = decoded_objects[0].data.decode('utf-8')
            result_label1.config(text=qr_data)

# QRコードを戻り値として返して、終了
def return_code():
    result = result_label1["text"]
    print(result)
    root.destroy()

# ウィンドウを作成
root = tk.Tk()
root.title("QRコードリーダー")
root.geometry ("600x400")

# 映像表示用のラベル
panel = ttk.Label(root)
panel.pack(padx=10, pady=10)
show_frame()

# ボタンを作成
button = tk.Button(root, text="QRコードを\n読み取る", command=read_qr_code, height=10, width=15, font=("MSゴシック", "10"))
button.pack(padx=10, pady=10, side=tk.LEFT)

button1 = tk.Button(root, text="確定", command=return_code, height=10, width=15, font=("MSゴシック", "10"))
button1.pack(padx=10, pady=10, side=tk.RIGHT)

# QRコードデータを表示するラベル
result_label = ttk.Label(root, text="QRコードデータ: ", font=("MSゴシック", "10", "bold"))
result_label.pack(padx=10, pady=10)

result_label1 = ttk.Label(root, text="", font=("MSゴシック", "20", "bold"))
result_label1.pack(padx=10, pady=30)

# ウィンドウを開始
root.mainloop()
