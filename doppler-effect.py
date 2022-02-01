import cv2
import numpy as np
import math


def img_hue_list(hsv_img):
	hue_list = []
	for row in hsv_img:
		for column in row:
			hue_list.append(column[0] * 2)
	return hue_list


def hue_to_wavelength(hue_list):
	wavelength_list = []
	for hue in hue_list:
		wavelength_list.append(int(700 - 300 / 270 * hue))
	return wavelength_list


def wavelength_to_hue(wavelength_list):
	hue_list = []
	for wavelength in wavelength_list:
		hue_list.append(int((wavelength - 700)/(-300 / 270)))
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


def doppler_effect_img(img_path, observor_speed): #observor_speed is relative to c (the speed of light)
	img = cv2.imread(img_path)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	hue_list = img_hue_list(img)
	wavelength_list = hue_to_wavelength(hue_list)

	wavelength_list = doppler_effect_formule(wavelength_list, observor_speed) 

	hue_list = wavelength_to_hue(wavelength_list)

	index = 0
	for row in img:
		for column in row:
			column[0] = hue_list[index] / 2
			index += 1

	img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
	cv2.imshow('img', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	


doppler_effect_img('./img.jpg', -0.1)




	