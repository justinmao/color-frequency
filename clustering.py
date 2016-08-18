import Image
import scipy
import scipy.misc
import scipy.cluster

NUM_CLUSTERS = 10


def read_image(im):
    # read_image(PIL image) -> representative numpy array
    im = im.resize((200, 200))  # faster processing (may lower accuracy)
    ar = scipy.misc.fromimage(im)
    shape = ar.shape
    # concatenate ar into a single array of rgb arrays, as opposed to a matrix
    return ar.reshape(shape[0]*shape[1], shape[2])


def rgb_to_hex(rgb):
    # converts an rgb tuple (255, 255, 255) to a hex string ffffff
    hex_string = ""
    for dec in rgb:
        hex_string += hex(dec).split("x")[1]
    return hex_string


def clusters(image_file, n):
    im = Image.open(image_file)
    ar = read_image(im)
    colors = []
    # generates a codebook using k-means algorithm for n clusters from ndarray
    codes = scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)[0]
    # array representation of a histogram
    count = scipy.histogram(scipy.cluster.vq.vq(ar, codes), len(codes))[0]

    i = 0
    while i < n:
        index = scipy.argmax(count)  # index of most occurring color
        if count[index] != 0:
            color = codes[index].astype(int)
            c_rgb = (color[0], color[1], color[2])
            c_hex = "".join(chr(c) for c in color).encode("hex")
            colors.append((c_rgb, c_hex))
            count[index] = 0
        i += 1
    return colors

print clusters("image.jpg", 2)