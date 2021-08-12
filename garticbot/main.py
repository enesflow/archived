# BGRRRRRR
from queue import Queue
from threading import Thread
import cv2
import numpy as np
import time
import pyautogui
import os

screenwidth = pyautogui.size().width
screenheight = pyautogui.size().height


def percentage(a, b):
    return a * b / 100


def main():
    inp = input(
        "Press [ENTER] to start drawing normally or type \"sketch\" and press [ENTER] to draw the image as like sketch (and possibly faster)")
    pyautogui.PAUSE = 0
    colors = [
        [0, 0, 0],
        [50, 50, 50],
        [255, 0, 0],
        [255, 255, 255],
        [200, 200, 200],
        [255, 255, 0],
        [0, 120, 0],
        [0, 0, 120],
        [0, 60, 150],
        [0, 255, 0],
        [0, 0, 255],
        [0, 120, 255],
        [0, 120, 200],
        [100, 0, 200],
        [100, 100, 150],
        [0, 255, 255],
        [127, 0, 255],
        [200, 127, 255]
    ]
    colorcoords = [
        [int(percentage(28.550512445095166, 1366)),
         int(percentage(45.57291666666667, 768))],
        [int(percentage(30.01464128843338, 1366)),
         int(percentage(45.57291666666667, 768))],
        [int(percentage(31.478770131771594, 1366)),
         int(percentage(45.57291666666667, 768))],
        [int(percentage(28.550512445095166, 1366)),
         int(percentage(48.56770833333333, 768))],
        [int(percentage(30.01464128843338, 1366)),
         int(percentage(48.56770833333333, 768))],
        [int(percentage(31.478770131771594, 1366)),
         int(percentage(48.56770833333333, 768))],
        [int(percentage(28.550512445095166, 1366)),
         int(percentage(51.5625, 768))],
        [int(percentage(30.01464128843338, 1366)),
         int(percentage(51.5625, 768))],
        [int(percentage(31.478770131771594, 1366)),
         int(percentage(51.5625, 768))],
        [int(percentage(28.550512445095166, 1366)),
         int(percentage(54.557291666666664, 768))],
        [int(percentage(30.01464128843338, 1366)),
         int(percentage(54.557291666666664, 768))],
        [int(percentage(31.478770131771594, 1366)),
         int(percentage(54.557291666666664, 768))],
        [int(percentage(28.550512445095166, 1366)),
         int(percentage(57.552083333333336, 768))],
        [int(percentage(30.01464128843338, 1366)),
         int(percentage(57.552083333333336, 768))],
        [int(percentage(31.478770131771594, 1366)),
         int(percentage(57.552083333333336, 768))],
        [int(percentage(28.550512445095166, 1366)),
         int(percentage(60.546875, 768))],
        [int(percentage(30.01464128843338, 1366)),
         int(percentage(60.546875, 768))],
        [int(percentage(31.478770131771594, 1366)),
         int(percentage(60.546875, 768))],
    ]

    def get_closest_color(img, index, h=0):
        def Average(lst):
            return sum(lst) / len(lst)
        pixels = {}
        for i in range(len(colors)):
            pixels[i] = []
        temp = img

        def for_loop(x):
            values = {}
            for color in colors:
                score = ((color[2]-x[2])**2 + (color[1]-x[1])
                         ** 2 + (color[0]-x[0])**2) ** 0.5
                values[colors.index(color)] = score
            best = 999
            best_index = 0
            for key, value in values.items():
                if value < best:
                    bestindex, best = key, value
            return colors[bestindex]
        for x in range(img.shape[1]):
            for y in range(img.shape[0]):
                j = for_loop(temp[y, x])
                temp[y, x] = j
                pixels[colors.index(j)].append([x, y + h])
        return pixels, index, temp

    name = "res.jpg"
    if os.path.exists("./res.png"):
        name = "res.png"
    img = cv2.imread(name, cv2.IMREAD_UNCHANGED)
    maxsize = 80
    x = max(max(img.shape[1] / maxsize, 1), max(img.shape[0] / maxsize, 1))
    img = cv2.resize(img, (0, 0), fx=1/x, fy=1/x)
    if name.split(".")[-1] == "png":
        try:
            trans_mask = img[:, :, 3] == 0
            img[trans_mask] = [255, 255, 255, 255]
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        except Exception as e:
            print(e)
    if inp == "sketch":
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_invert = cv2.bitwise_not(img_gray)
        img_smoothing = cv2.GaussianBlur(
            img_invert, (21, 21), sigmaX=0, sigmaY=0)

        def dodgeV2(x, y):
            return cv2.divide(x, 255 - y, scale=256)
        img = dodgeV2(img_gray, img_smoothing)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    h, w, c = img.shape
    print(w, h)

    tm = time.time()
    up_half = img[0:int(h/2), 0:w]
    down_half = img[int(h/2):h, 0:w]
    que = Queue()

    threads_list = list()

    t = Thread(target=lambda q, arg1: q.put(
        get_closest_color(up_half, 0)), args=(que, 0))
    t.start()
    threads_list.append(t)
    t1 = Thread(target=lambda q, arg1: q.put(
        get_closest_color(down_half, 1, int(h / 2))), args=(que, 1))
    t1.start()
    threads_list.append(t1)

    for t in threads_list:
        t.join()
    imgs = {}
    raw_pixels = {}
    for i in range(len(colors)):
        raw_pixels[i] = []
    while not que.empty():
        result, i, image = que.get()
        if i == 0:
            up_half = image
        else:
            down_half = image
        imgs[i] = result

    for key, val in raw_pixels.items():
        raw_pixels[key] = imgs[0][key] + imgs[1][key]

    raw_pixels[3] = []
    pixels = {k: v for k, v in (sorted(
        raw_pixels.items(), key=lambda item: len(item[1])))[::-1]}
    final_pixels = {k: v for k, v in (sorted(
        raw_pixels.items(), key=lambda item: len(item[1])))[::-1]}

    print(time.time() - tm)
    # cv2.imshow("aa", up_half)
    # cv2.imshow("ab", down_half)
    # cv2.imshow("aa", np.vstack((imgs[0], imgs[1])))
    # cv2.waitKey(0)
    time.sleep(3)
    x, y = pyautogui.position()
    smallsize = 643
    pyautogui.click(395, smallsize)
    for key, value in final_pixels.items():
        pyautogui.click(colorcoords[key])
        for i in value:
            pyautogui.click(x + (i[0] * 4), y + (i[1] * 4))

    os.rename(name, "DONE "+str(time.time()) + "." + name.split(".")[-1])
    main()


if __name__ == "__main__":
    main()
