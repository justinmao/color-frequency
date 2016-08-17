from PIL import Image


def get_main_colors(file):
    im = Image.open(file)
    colors = im.getcolors(im.size[0]*im.size[1])
    max_occ = 0
    main_color = 0
    secondary_color = 0
    tertiary_color = 0

    for c in colors:
        if c[0] > max_occ:
            tertiary_color = secondary_color
            secondary_color = main_color
            (max_occ, main_color) = c
    print "Main color: " + str(main_color)
    if secondary_color != 0:
        print "Secondary color: " + str(secondary_color)
        if tertiary_color != 0:
            print "Tertiary color: " + str(tertiary_color)

image_file = raw_input("File name: ")
get_main_colors(image_file)