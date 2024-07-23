import cv2
import numpy as np

def recognize_digits(image):
    # 画像の前処理
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 輪郭検出
    edges = cv2.Canny(blurred, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 数字候補のフィルタリング
    digits = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        if area > 100 and w > 10 and h > 10:
            digits.append((x, y, w, h))

    # 数字の認識
    predictions = []
    for x, y, w, h in digits:
        roi = gray[y:y+h, x:x+w]
        avg = np.mean(roi)
        prediction = int(avg / 255)
        predictions.append(prediction)

    # 結果の表示
    for x, y, w, h, prediction in zip(digits, predictions):
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, str(prediction), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Result', image)
    cv2.waitKey(0)

# テスト画像
image = cv2.imread('C:/Users/29004/Desktop/Sample.png')

# 数字認識処理の実行
recognize_digits(image)