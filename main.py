
import colorgram

colors = colorgram.extract("image.jpg", 6)
color_array = []
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    color_array.append((r, g, b))
print(color_array)