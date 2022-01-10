#author: animesh
#this file is to execuate and get the output of the image you wish to get.
#this is the final result


from os import listdir
from keras.models import load_model
from numpy import asarray, load
from keras.preprocessing.image import img_to_array
from numpy.random import randint
from numpy import vstack
from matplotlib import pyplot
from keras.preprocessing.image import load_img



# load all images in a directory into memory
def load_images(path, size=(256, 512)):
    src_list = list()
    # enumerate filenames in directory, assume all are images
    for filename in listdir(path):
        # load and resize the image
        pixels = load_img(path + filename, target_size=size)
        # convert to numpy array
        pixels = img_to_array(pixels)
        # split into satellite and map
        sat_img, map_img = pixels[:, :256], pixels[:, 256:]
        src_list.append(sat_img)
        #tar_list.append(map_img)
    return [asarray(src_list)]


def preprocess_data(data):
    # load compressed arrays
    # unpack arrays
    X1 = data[0]
    # scale from [0,255] to [-1,1]
    X1 = (X1 - 127.5) / 127.5
    #X2 = (X2 - 127.5) / 127.5
    return [X1]

# plot source, generated and target images
def plot_images(src_img, gen_img):
    images = vstack((src_img, gen_img))
    # scale from [-1,1] to [0,1]
    images = (images + 1) / 2.0
    titles = ['Source', 'Generated']
    # plot images row by row
    for i in range(len(images)):
        # define subplot
        pyplot.subplot(1, 3, 1 + i)
        # turn off axis
        pyplot.axis('off')
        # plot raw pixel data
        pyplot.imshow(images[i])
        # show title
        pyplot.title(titles[i])
    pyplot.show()


#path = 'maps/train/'
path = "maps/exc/"     #put the folder name of the dir where you have kept your satelite images
# load dataset
[src_images] = load_images(path)

model = load_model('model_010960.h5')
data = [src_images]


dataset = preprocess_data(data)
[X1] = dataset
# select random example
ix = randint(0, len(X1), 1)
src_image = X1[ix]
# generate image from source
gen_image = model.predict(src_image)
# plot all three images
plot_images(src_image, gen_image)

