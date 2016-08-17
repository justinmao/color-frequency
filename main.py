from PIL import Image

# takes an rgb tuple (255, 255, 255)
# returns a hex string FFFFFF
def rgb_to_hex(rgb):
    hex_string = ""
    for dec in rgb:
        hex_string += hex(dec).split("x")[1]
    return hex_string

# takes a file and finds the n top occurring RGB values specified
# returns a list of tuples [((255, 255, 255), FFFFFF, % occurrence), ...]
def run(file, n):
    im = Image.open(file)
    colors = im.getcolors(im.size[0] * im.size[1])
    max_occ = 0
    li = []

    for c in colors:
        if c[0] > max_occ:
            li.insert(0, (c[1], rgb_to_hex(c[1]), round(100.0*c[0]/len(colors), 2)))
            max_occ = c[0]

    i = 0
    while i < n:
        print li[i]
        i += 1

image_file = raw_input("File name: ")
n = input("Number of top colors: ")
run(image_file, n)