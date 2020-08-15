# -*- coding=utf-8 -*-
import cv2

facePath = "./xml/haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(facePath)

smilePath = "./xml/haarcascade_smile.xml"
smileCascade = cv2.CascadeClassifier(smilePath)

img = cv2.imread("./image/test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=8,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# 畫出每一個臉
for (x, y, w, h) in faces:
    #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # 對人臉進行微笑偵測
    smile = smileCascade.detectMultiScale(
        roi_gray,
        scaleFactor= 1.16,
        minNeighbors=35,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # 框出上揚嘴角，並打上 Smile 標籤
    print(smile)
    for (x2, y2, w2, h2) in smile:
        cv2.rectangle(roi_color, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 2)
        cv2.putText(img, 'Smile', (x+x2, y+y2-7), 3, 1.2, (0, 255, 0), 2)

    if len(smile) == 0:
        cv2.putText(img, 'No Smile', (x, y - 7), 3, 1.2, (0, 0, 255), 2)

cv2.imshow('Smile', img)
# 儲存檔案
cv2.imwrite("./result/smile.jpg",img)
# 任意鍵離開(若設定為 0 就表示持續等待至使用者按下按鍵為止)
c = cv2.waitKey(0)
