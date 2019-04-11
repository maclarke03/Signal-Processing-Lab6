# Micah Clarke
# ID: 1001288866

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import skimage.feature.template as sft


def findImage(mainImage, template) :
  
    
    def rgb2gray(rgb):
       return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

    # Read in mainImage, convert to gray scale and plot
    mainImagePic = mpimg.imread(mainImage)     
    mainGrayValues = rgb2gray(mainImagePic)
    plt.imshow(mainGrayValues, cmap=plt.get_cmap('gray'))
    plt.show()
    # Read in templateImage, convert to gray scale and plot
    templateImagePic = mpimg.imread(template)     
    templateGrayValues = rgb2gray(templateImagePic)
    plt.imshow(templateGrayValues, cmap = plt.get_cmap(name = 'gray'))
    plt.show()
    
    # Calculate number of rows and columns in template image
    numrows = len(templateGrayValues)
    numcols = len(templateGrayValues[0])
    # Assign 2D zero array for zero-ing out matched image indexes
    zeroArray = np.zeros(shape=(numrows+1,numcols+1))
    # Cross-correlation function
    result = sft.match_template(mainGrayValues,templateGrayValues)
    # Determine which row and column where the highest normalized cross-correlation occurs at
    row = np.argmax(np.max(result, axis=1))
    col = np.argmax(np.max(result, axis=0))
    print("\n\nCoordinates within the larger image with the highest normalized cross-correlation: \n","(",row,",",col,")")
    # Black out the larger image where the template image is at
    mainGrayValues[row:row+numrows+1,col:col+numcols+1] = zeroArray
    mainGrayValues = mainGrayValues.astype(int)
    finalImage = Image.fromarray(mainGrayValues)
    plt.imshow(finalImage)
    plt.show()
    
 
#############  main  #############
if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"
    findImage(mainImage, template)
