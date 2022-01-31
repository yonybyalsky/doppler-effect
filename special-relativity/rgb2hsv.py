import cv2
import numpy as np

img = cv2.imread('./green.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hue_arr = []

for row in img:
	for column in row:
		hue_arr.append(column[0] * 2)

wavelength_arr = []

for hue in hue_arr:
	wavelength_arr.append(int(650 - 250 / 270 * hue))

i = 0
while i <= len(wavelength_arr) - 1:
	wavelength_arr[i] += 80
	i += 1

print(wavelength_arr)

new_hue_arr = []

for wavelength in wavelength_arr:
	new_hue_arr.append(int((wavelength - 650) / (-250 / 270)))
 
index = 0

for row in img:
	for column in row:
		column[0] = new_hue_arr[index] / 2
		index += 1


img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
