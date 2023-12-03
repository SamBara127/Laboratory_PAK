import numpy as np
import cv2
from matplotlib import pyplot as plt

def fill_rectangle(r, img):
    '''

    paints contour "r" in black on img

    :param r: np.ndarray
    :param img: Image
    :return:
    img : Image
    '''
    contours = [np.array(r, dtype=np.int32)]
    cv2.drawContours(img, contours, -1, (0, 0, 0), cv2.FILLED)
    return img


def detect_images(result_img, main_img, img_1):

    # для обнаружения ключевых точек будем использовать алгоритм SIFT
    sift = cv2.SIFT_create()

    # применяем оттенок серого для ускорения работы SIFT посредством сжимания 3 канала в 1-черно-белый
    # без потерь возможности детектирования ключевых точек
    main_gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
    gray_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

    # нахождение ключевых точек на изображении и их дескрипторов-уникальной "карты"
    # градиентов контраста в радиусе данных точек
    keypoints_main, descriptors_main = sift.detectAndCompute(main_gray, None)
    keypoints_1, descriptors_1 = sift.detectAndCompute(gray_1, None)

    # result = img_1.copy()
    # result = cv2.drawKeypoints(img_1, keypoints_1, result)

    # Затем нам необходимо сопоставить(вычислить расстояние) дискрипторы изображения призраков с дискрипторами основного
    # в этом поможет BFMatcher, который осуществляетпоиск наиболее похожего дескриптора на разных изображениях
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    matches = bf.match(descriptors_1, descriptors_main)
    matches = sorted(matches, key = lambda x:x.distance)

    rect = []
    src_pts = np.float32([keypoints_1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([keypoints_main[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    h, w, _ = img_1.shape
    pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, M)
    #
    for i in range(4):
        rect.append([int(dst[i][0][0]), int(dst[i][0][1])])

    main_img = cv2.polylines(main_img, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
    result_img = cv2.polylines(result_img, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

    return result_img, fill_rectangle(rect, main_img)
    # img_out = cv2.drawMatches(img_1, keypoints_1, main_img, keypoints_main, matches[:20], None, flags=2)

if __name__ == '__main__':
    # считываем изображения в массив изображения
    main_img = cv2.imread('lab72.png')
    img_1 = cv2.imread('scary_ghost.png')
    img_2 = cv2.imread('pampkin_ghost.png')
    img_3 = cv2.imread('candy_ghost.png')

    result_img = main_img.copy()
    
    result_img, main_img= detect_images(result_img, main_img, img_1)
    result_img, main_img= detect_images(result_img, main_img, img_1)
    result_img, main_img= detect_images(result_img, main_img, img_2)
    result_img, main_img= detect_images(result_img, main_img, img_3)
    result_img, main_img= detect_images(result_img, main_img, img_3)
    result_img, main_img= detect_images(result_img, main_img, img_3)

    cv2.imshow('scary_ghost', result_img)
    while(1):
        if cv2.waitKey(10) == 27:  # Клавиша Esc
            break
    cv2.destroyAllWindows()