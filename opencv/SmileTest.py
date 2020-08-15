import cv2

print(cv2.__version__)
# 人臉偵測器
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')
# 眼睛偵測
eye_cascade = cv2.CascadeClassifier('./xml/haarcascade_eye.xml')
# 微笑偵測
smile_cascade = cv2.CascadeClassifier('./xml/haarcascade_smile.xml')

# 設定攝像鏡頭
cap = cv2.VideoCapture(1)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # 捕捉 frame-by-frame
    ret, frame = cap.read()  # ret : 讀到的 frame 是正確的話會回傳 true

    # 定義灰度圖像 (cvtColor 讓影像在不同色彩空間中轉換)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 畫出每一個臉的範圍
    faces = face_cascade.detectMultiScale(
        gray,  # 待檢測圖片，一般為灰度圖像加快檢測速度
        scaleFactor=1.1,  # 檢測粒度 scaleFactor 。更大的粒度將會加快檢測的速度，但是會對檢測準確性產生影響。
        # 相反的，一個更小的粒度將會影響檢測的時間，但是會增加準確性。
        # 運作：在前後兩次相繼的掃描中，搜尋視窗的比例係數。預設為1.1，即每次搜尋視窗依次擴大10%
        minNeighbors=5,  # 每個目標至少檢測到幾次以上，才可被認定是真數據。
        minSize=(30, 30),  # 設定數據搜尋的最小尺寸 ，如 minSize=(30,30)，也就是太小的臉就忽略辨識
        flags=cv2.CASCADE_SCALE_IMAGE  # CASCADE_SCALE_IMAGE=2 -> 正常比例檢測
        # CASCADE_DO_CANNY_PRUNING=1 -> 利用canny邊緣檢測來排除一些邊緣很少或者很多的影象區域
        # CASCADE_FIND_BIGGEST_OBJECT=4 -> 只檢測最大的物體
        # CASCADE_DO_ROUGH_SEARCH=8 粗略的檢測
    )
    # 在臉部周圍畫矩形框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)  # 注意：(0, 255, 0) 是 BGR
        # 繪文字
        cv2.putText(frame, 'Vincent', (x, y - 7), 2, 1.2, (0, 255, 0), 2)

        # 獲取該人臉矩形框的感興趣區域 ROI(region of interest), 淺複製(子圖像區域)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=15,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # 眼睛的最底部
        myeyesY = 0
        for (ex, ey, ew, eh) in eyes:
            myeyesY = ey + eh
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

        # 對人臉進行微笑偵測
        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=100,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # 框出上揚嘴角
        for (sx, sy, sw, sh) in smile:
            if (myeyesY > 0 and sy > myeyesY):
                cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 2)

    # 將 frame 顯示
    cv2.imshow('Video', frame)

    # 按下 q 離開迴圈 (「1」表示停 1ms 來偵測是否使用者有按下q。若設定為「0」就表示持續等待至使用者按下按鍵為止)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源與關閉視窗
cap.release()
cv2.destroyAllWindows()
