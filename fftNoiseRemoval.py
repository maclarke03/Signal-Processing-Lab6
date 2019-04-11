# Micah Clarke
# ID: 1001288866

import numpy as np
import math
import matplotlib.pyplot as plt
import soundfile as sf

def processFile(fn, offset) :
    # In case the signal had an odd number of values instead of even being used
    even = False
    # Read in signal from wavfile
    signal, fs = sf.read(fn)
    # Apply FFT
    fftSignal = np.fft.fft(signal)
    plt.subplot(1,2,1)
    plt.plot(abs(fftSignal))
    plt.title("Noisy")

    
    # Find the midpoint of the FFT values
    middle = (len(fftSignal))/2
    # If the signal has an even # of values grab the two remaining middle points
    if len(fftSignal) % 2 == 0:
        even = True
        middle1 = int(middle)
        middle2 = middle1 - 1

    # If the signal has an odd # of values grab the middle
    else:
        middle1 = int(math.floor(middle))
        
    # Apply zeros depending on the offset size
    zeros = np.zeros(offset+1)

    # If the signal has an even number of values we need to zero the offset pairs on each
    # side of middle1 and middle2
    if even == True:
        fftSignal[middle1:middle1+offset+1] = zeros
        fftSignal[middle1-offset:middle1+1] = zeros
        fftSignal[middle2:middle2+offset+1] = zeros
        fftSignal[middle2-offset:middle2+1] = zeros
        #print(fftSignal[middle2-offset:middle1+offset+1])

    # If the signal has an odd number of values we need to just zero out the offset pairs on
    # each side of the middle
    else:
        fftSignal[middle:middle+offset+1] = zeros
        fftSignal[middle-offset:middle+1] = zeros

    # Apply inverse FFT to create new, clean signal
    ifftSignal = np.fft.ifft(fftSignal)

    sf.write('cleanMusic.wav', ifftSignal.real, fs)

    plt.subplot(1,2,2)
    plt.plot(abs(fftSignal))
    plt.title("Clean")
    plt.show()
        
    


##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav"
    offset = 10000

    # this function should be how your code knows the name of
    #   the file to process and the offset to use
    processFile(filename, offset)
