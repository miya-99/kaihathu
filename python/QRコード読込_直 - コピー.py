import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
barcodes = []
flg = 0


while cap.isOpened():
    ret, frame = cap.read()

    cap.protocol("WM_DELETE_WINDOW",cap.delete_window)

    if ret:
        d = decode(frame)

        if d:
            for barcode in d:
                barcodeData = barcode.data.decode('utf-8')
                if barcodeData not in barcodes:
                    result = barcodeData
                    print(result)
                    flg = 1

                x, y, w, h = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), font_color, 2)
                frame = cv2.putText(frame, barcodeData, (x, y - 10), 
                                    font, .5, font_color, 2, cv2.LINE_AA)

    cv2.imshow('BARCODE READER', frame)

    if flg == 1:
        break

    def delete_window(cap):
        print("ウィンドウのxボタンが押された")

        # 終了確認のメッセージ表示
        ret = messagebox.askyesno(
            title = "終了確認",
            message = "プログラムを終了しますか？")

        if ret == True:
            # 「はい」がクリックされたとき
            cap.master.destroy()
	
	#キー入力を待ち、'q'または✕ボタンが押されたらループを抜ける
#    key = cv2.waitKey(1)
#    print(key)
#    if key & 0xFF == ord('q') or key & 0xFF == 27 :
#    if key & 0xFF == ord('q') or key == 27 :
#        break

cap.release()
cv2.destroyAllWindows()
#print (barcodeData)
#return (barcodeData)
