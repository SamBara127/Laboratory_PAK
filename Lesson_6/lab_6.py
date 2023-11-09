import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)

_, green_backgr = cap.read()
green_backgr[...] = [0, 80, 0]

flg = 1

while True:
    ret1, img1 = cap.read()
    ret2, img2 = cap.read()
    # filter images
    img1 = cv2.GaussianBlur(img1, (3, 3), 30) # фильтрация Гаусса
    img2 = cv2.GaussianBlur(img2, (3, 3), 30) # фильтрация Гаусса
    img1 = cv2.medianBlur(img1, 3) # сглаживание по краям
    img2 = cv2.medianBlur(img2, 3) # сглаживание по краям
    #
    if flg == 1:
        diff = cv2.absdiff(img1, img2)  # разница между 2 кадрами
        wh = np.where(
            (diff[:, :, 0] > 10) &
            (diff[:, :, 1] > 10) &
            (diff[:, :, 2] > 10)
        )  # уменьшаем реакцию в увеличении шага восприятия разницы в цвете
        diff[wh] = [0, 0, 255]
        img1 = cv2.addWeighted(green_backgr, 1, img1, 1, 0.0)     #вычисляет сумму 2 массивов матрицы изображения
        res = cv2.addWeighted(diff, 1, img1, 1, 0.0)   #вычисляет сумму 2 массивов матрицы изображения
    else:
        res = cv2.addWeighted(green_backgr, 1, img1, 1, 0.0)    #вычисляет сумму 2 массивов матрицы изображения
    cv2.imshow("camera", res)   # рендеринг и вывод массива изображения в виде изображения на экран
    flg = flg * (-1)
    if cv2.waitKey(10) == 27:  # Клавиша Esc
        break

cap.release()
cv2.destroyAllWindows()
