from matplotlib.image import imread
from matplotlib.image import imsave
from matplotlib import pyplot as plt
from glob import glob

import numpy as np
import os

def compress(grayscale_img,keep):
    B = np.mean(grayscale_img, -1)
    Bt = np.fft.fft2(B)
    Btsort = np.sort(np.abs(Bt.reshape(-1)))
    thresh = Btsort[int(np.floor((1-keep)*len(Btsort)))]
    ind = np.abs(Bt)>thresh
    Btlow = Bt * ind
    Alow = np.fft.ifft2(Btlow).real
    return Alow

if __name__ == "__main__":
    os.chdir("input")
    file_names = glob('*')
    os.chdir("..")
    keep=float(input(("\nWhat % of the fourier coefficients do you want to keep?: ")))
    compressed_mat=[]
    for i in range(len(file_names)):
        os.chdir("input")
        print("----Compressing:   "+file_names[i])
        compressed = compress (imread(file_names[i]),keep/100)
        os.chdir("..")
        os.chdir("output")
        imsave('compressed_'+file_names[i],compressed,cmap='gray')
        os.chdir("..")
