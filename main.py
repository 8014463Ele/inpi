variable = 2

display.clear()

 (x, y, brightness 0-9)
if variable > 2:
display.set_pixel(3, 2, 9)
display.set_pixel(4, 2, 9)
elif variable < 2:
display.set_pixel(0, 2, 9)
display.set_pixel(1, 2, 9)
else:
display.set_pixel(2, 2, 9)
