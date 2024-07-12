import cv2
from pyzbar.pyzbar import decode
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
barcodes = []
flg = 0

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        d = decode(frame)

        if d:
            for barcode in d:
                barcodeData = barcode.data.decode('utf-8')
                font_color = (0, 154, 87)
                if barcodeData not in barcodes:
                    result = barcodeData
                    print(result)
                    flg = 1

                x, y, w, h = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), font_color, 2)
                frame = cv2.putText(frame, barcodeData, (x, y - 10), 
                                    font, .5, font_color, 2, cv2.LINE_AA)

    cv2.imshow('BARCODE READER (quit:q)', frame)

    if flg == 1:
    	break

#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

    #キー入力を待ち、'q'または✕ボタンが押されたらループを抜ける
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27 :
        break

cap.release()
#print (barcodeData)
#return (barcodeData)
