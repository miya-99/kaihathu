import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
BUF_FILE_PATH = r'./buf.txt'
barcodes = []

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        d = decode(frame)

        if d:
            for barcode in d:
                barcodeData = barcode.data.decode('utf-8')

                if barcodeData not in barcodes:
                    barcodes.append(barcodeData)
                    font_color = (0, 0, 255)
                    with open(BUF_FILE_PATH, mode='a') as buf:
                        buf.write(barcodeData + '\n')
                else:
                    font_color = (0, 154, 87)

                x, y, w, h = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), font_color, 2)
                frame = cv2.putText(frame, barcodeData, (x, y - 10), 
                                    font, .5, font_color, 2, cv2.LINE_AA)

    cv2.imshow('BARCODE READER', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
