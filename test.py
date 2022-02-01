def hue_to_wavelength(hue):
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

	return w

def wavelength_to_hue(w):
	if w >= 400 and w <= 430:
		h = 670 - w

	elif w >= 430 and w <= 485:
		h = (-w + 55/30*180 + 485)/(55/30)

	elif w >= 485 and w <= 500:
		h = (-w + 15/30*150 + 500)/(15/30)

	elif w >= 500 and w <= 565:
		h = (-w + 65/30*90 + 565)/(65/30)

	elif w >= 565 and w <= 590:
		h = (-w + 25/30*60 + 590)/(25/30)

	elif w >= 590 and w <= 625:
		h = (-w + 35/30*30 + 625)/(35/30)

	elif w >= 625 and w <= 700:
		h = (-w + 700)/(75/30)

	return h

for w in range(400, 700, 50):
	print(w, wavelength_to_hue(w))