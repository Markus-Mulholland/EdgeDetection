from PIL import Image

img_name = "Ellipse"

# access images
img = Image.open(img_name + ".jpg")
width, height = img.size
img = img.convert("1")

img1, img2 = Image.new("1", (width, height)), Image.new("1", (width, height))

# load pixels
pixels, pixels1, pixels2 = img.load(), img1.load(), img2.load()

# filter and build new image
i, j = 0, 0
while i < width:
    while j < height:
        lum = pixels[i, j]

        if j + 1 > height - 1:
            lum1 = lum
        else:
            lum1 = pixels[i, j + 1]

        lum_diff = lum-lum1

        if lum_diff > 0:
            pixels1[i, j] = 0
            pixels1[i, j + 1] = 255
            j += 1
        elif lum_diff < 0:
            pixels1[i, j] = 255
        else:
            pixels1[i, j] = 0

        j += 1

    j = 0
    i += 1

i, j = 0, 0
while j < height:
    while i < width:
        lum = pixels[i, j]

        if i + 1 > width - 1:
            lum1 = lum
        else:
            lum1 = pixels[i + 1, j]

        lum_diff = lum-lum1

        if lum_diff > 0:
            pixels2[i, j] = 0
            pixels2[i + 1, j] = 255
            i += 1
        elif lum_diff < 0:
            pixels2[i, j] = 255
        else:
            pixels2[i, j] = 0

        i += 1

    i = 0
    j += 1

img1.save(img_name + "_bounds" + ".jpg", 'JPEG')
img2.save(img_name + "_bounds1" + ".jpg", 'JPEG')

img = Image.new("1", (width, height))

pixels, pixels1, pixels2 = img.load(), img1.load(), img2.load()

for i in range(width):
    for j in range(height):
        pixels[i, j] = 255 if pixels1[i, j] + pixels2[i, j] >= 255 else 0

img.save(img_name + "_final" + ".jpg", 'JPEG')



