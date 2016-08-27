import Image
import scipy
import scipy.misc
import scipy.cluster
import urllib
import cStringIO

NUM_CLUSTERS = 20


def read_image(im):
    # read_image(PIL image) -> representative numpy array
    im = im.resize((100, 100))  # faster processing (may lower accuracy)
    ar = scipy.misc.fromimage(im)
    shape = ar.shape
    # concatenate ar into a single array of rgb arrays, as opposed to a matrix
    return ar.reshape(shape[0]*shape[1], shape[2])


def get_palette(url, n):
    # url(image), n(colors) -> list of n dominant colors
    # does not check for validity of url nor checks for n > NUM_CLUSTERS!
    image_file = cStringIO.StringIO(urllib.urlopen(url).read())
    im = Image.open(image_file)
    ar = read_image(im)
    colors = []
    # generates a codebook using k-means algorithm for n clusters from ndarray
    codes = scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)[0]
    print codes
    # sorted array representation of a histogram
    count = scipy.histogram(scipy.cluster.vq.vq(ar, codes), len(codes))[0]
    print count
    for i in range(int(n)):
        index = scipy.argmax(count)  # index of most occurring color
        if count[index] != 0:
            color = codes[index].astype(int)
            c_rgb = (color[0], color[1], color[2])
            c_hex = "".join(chr(c) for c in color).encode("hex")
            colors.append((c_rgb, c_hex))
            count[index] = 0
    return colors
