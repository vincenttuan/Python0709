import cv2  # 安裝 py-opencv
import requests
import sys

# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt.xml
eyes_cascade = cv2.CascadeClassifier('./xml/haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # 捕捉 frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 畫出每一個臉的範圍
    eyes = eyes_cascade.detectMultiScale(
        gray,              # 待檢測圖片，一般為灰度圖像加快檢測速度
        scaleFactor=1.1,   # 檢測粒度 scaleFactor 。更大的粒度將會加快檢測的速度，但是會對檢測準確性產生影響。相反的，一個更小的粒度將會影響檢測的時間，但是會增加準確性。
        minNeighbors=5,    # 每個目標至少檢測到幾次以上，才可被認定是真數據。
        minSize=(30, 30),  # 設定數據搜尋的最小尺寸 ，如 minSize=(30,30)
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print(eyes)
    # 在眼部周圍畫矩形框
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)  # 注意：(0, 255, 0) 是 BGR

    # 將 frame 顯示
    cv2.imshow('Video', frame)

    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

