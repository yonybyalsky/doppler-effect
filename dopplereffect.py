import cv2
import numpy as np
import math


def img_hue_list(hsv_img):
    hue_list = []
    for row in hsv_img:
        for column in row:
            hue_list.append(column[0] * 2)
    return hue_list


def hue_to_wavelength(hue):
    w = 0
    if hue >= 0 and hue <= 30:
        w = int(700 - 75/30 * hue)

    elif hue >= 30 and hue <= 60:
        w = int(625 - 35/30 * (hue - 30))

    elif hue >= 60 and hue <= 90:
        w = int(590 - 25/30 * (hue - 60))

    elif hue >= 90 and hue <= 150:
        w = int(565 - 65/30 * (hue - 90))

    elif hue >= 150 and hue <= 180:
        w = int(500 - 15/30 * (hue - 150))

    elif hue >= 180 and hue <= 240:
        w = int(485 - 55/30 * (hue - 180))

    elif hue >= 240 and hue <= 270:
        w = int(430 - 30/30 * (hue - 240))
    elif hue > 270 and hue < 300:
        w = 400
    elif hue > 270 and hue < 300:
        w = 400
    elif hue > 300:
    	w = 700

    return w


def wavelength_to_hue(w):
    h = 0
    if w >= 400 and w <= 430:
        h = int(670 - w)

    elif w >= 430 and w <= 485:
        h = int((-w + 55/30*180 + 485)/(55/30))

    elif w >= 485 and w <= 500:
        h = int((-w + 15/30*150 + 500)/(15/30))

    elif w >= 500 and w <= 565:
        h = int((-w + 65/30*90 + 565)/(65/30))

    elif w >= 565 and w <= 590:
        h = int((-w + 25/30*60 + 590)/(25/30))

    elif w >= 590 and w <= 625:
        h = int((-w + 35/30*30 + 625)/(35/30))

    elif w >= 625 and w <= 700:
        h = int((-w + 700)/(75/30))

    elif w > 700:
        h = 0

    elif w < 400:
        h = 270

    return h


def hue_to_wavelen_list(hue_list):
    wavelength_list = []
    for hue in hue_list:
        wavelength_list.append(hue_to_wavelength(hue))
    return wavelength_list


def wavelen_to_hue_list(wavelength_list):
    hue_list = []
    for wavelength in wavelength_list:
        hue_list.append(wavelength_to_hue(wavelength))
    return hue_list


def doppler_effect_formule(wavelength_list, observor_speed):
    c = 3e8
    v = observor_speed * c
    i = 0
    while i <= len(wavelength_list) - 1:
        wavelength_list[i] *= math.sqrt((1 + v/c)/(1 - v/c))
        if wavelength_list[i] > 700:
            wavelength_list[i] = 700
        if wavelength_list[i] < 400:
            wavelength_list[i] = 400
        i += 1
    return wavelength_list


# observor_speed is relative to c (the speed of light)
def doppler_effect_img(img_path, observor_speed):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hue_list = img_hue_list(img)
    print(hue_list[0])
    wavelength_list = hue_to_wavelen_list(hue_list)
    print(wavelength_list[0])
    wavelength_list = doppler_effect_formule(wavelength_list, observor_speed)
    print(wavelength_list[0])
    hue_list = wavelen_to_hue_list(wavelength_list)
    print(hue_list[0])
    index = 0
    for row in img:
        for column in row:
            column[0] = hue_list[index] / 2
            index += 1

    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

    return img


img = doppler_effect_img('./green.png', 0.1)

# img = cv2.resize(img, (600, 600))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
