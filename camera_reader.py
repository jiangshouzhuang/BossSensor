# -*- coding:utf-8 -*-
import cv2

from boss_train import Model
from image_show_pyqt5 import show_image


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    #cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    cascade_path = "/Users/zhangyun/anaconda/anaconda3/anaconda3/envs/python35/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    model = Model()
    model.load()
    while True:
        _, frame = cap.read()

        # 灰度转换
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 获取级联分类器的特征值
        cascade = cv2.CascadeClassifier(cascade_path)

        # 执行物体识别（人脸识别）
        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
        #facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(3, 3))
        if len(facerect) > 0:
            print('face detected')
            color = (255, 255, 255)  # 白
            for rect in facerect:
                # 在检测到的面部周围创建一个矩形
                #cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

                x, y = rect[0:2]
                width, height = rect[2:4]
                image = frame[y - 10: y + height, x: x + width]

                result = model.predict(image)
                if result == 0:  # boss
                    print('Boss is approaching')
                    show_image()
                else:
                    print('Not boss')

        #等待10毫秒键输入
        k = cv2.waitKey(100)
        #按Esc退出
        if k == 27:
            break

    # 结束捕获
    cap.release()
    cv2.destroyAllWindows()
