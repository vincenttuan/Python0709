# 匯入所需程式庫
import cv2
from faceid import A_參數設定

# 載入 Config.HAAR_FACES 指定的層疊分類器
face_cascade = cv2.CascadeClassifier(A_參數設定.HAAR_FACES)

if __name__ == '__main__':
    # 取得攝像鏡頭位置
    cap = cv2.VideoCapture(0)

    # 設定攝像鏡頭捕捉區域
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 列印訓練集資料載入中訊息
    print('訓練集資料載入中 ...')

    # 依 Config.COMPONENT_NUMBER 指定的特徵數量、Config.POSITIVE_THRESHOLD 允收距離，來建立特徵臉鑑別器
    model = cv2.face.EigenFaceRecognizer_create(A_參數設定.COMPONENT_NUMBER, A_參數設定.POSITIVE_THRESHOLD)

    # 載入 Config.TRAINING_FILE 指定的訓練集檔案
    model.read(A_參數設定.TRAINING_FILE)

    # 列印訓練集資料完成載入訊息
    print('訓練集資料載入完成 !')

    # 開始循環偵測
    while True:
        # 捕捉 frame-by-frame
        ret, frame = cap.read()  # ret : 讀到的 frame 是正確的化會回傳 true

        # 定義灰度圖像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 監測人臉
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # 找到的人臉個數
        print("Found {0} faces!".format(len(faces)))

        # 在臉部周圍畫矩形框
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)  # 注意：(0, 255, 0) 是 BGR


        # 按下 q 離開迴圈 (「1」表示停 1ms 來偵測是否使用者有按下q。若設定為「0」就表示持續等待至使用者按下按鍵為止)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # 開始辨識程序...begin

        # 1.判斷是否為單一人臉的圖片
        result = A_參數設定.detect_single(gray, face_cascade)

        # 2.判斷 result 有無回傳值
        if result is None:
            print('無法偵測到單一人臉 opencv_faceid !')
            # 將 frame 顯示
            cv2.imshow('Detect face', frame)
            # 重新偵測
            continue

        # 3.取得欲裁切的資料
        x, y, w, h = result

        # 4.進行裁切放人臉圖片
        crop = A_參數設定.resize(A_參數設定.crop(gray, x, y, w, h))

        # 5.進行比對檢驗評估
        label = model.predict(crop)

        # 6.列印評估資訊
        print(label)

        # 7.判斷評估值 <= Config.POSITIVE_THRESHOLD
        if label[1] <= A_參數設定.POSITIVE_THRESHOLD:
            # 印出辨識成功
            print('辨識成功 opencv_faceid!')
            for (x, y, w, h) in faces:
                # 繪文字
                cv2.putText(frame, 'OK', (x, y - 7), 16, 1.2, (0, 255, 0), 2)
            # 跳出循環偵測回圈
            # break
        else:
            # 印出辨識失敗
            print('辨識失敗 opencv_faceid!')
            for (x, y, w, h) in faces:
                # 繪文字
                cv2.putText(frame, 'Error', (x, y - 7), 16, 1.2, (0, 255, 0), 2)

        # 結束辨識程序...end

        # 將 frame 顯示
        cv2.imshow('Detect face', frame)

    # 釋放資源
    cap.release()

    # 關閉所有視窗
    cv2.destroyAllWindows()
