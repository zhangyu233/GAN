#In this test case, the ground truth time sequences are arithmetic progression starting from 1
#That is to say, '1 3 5 7' is a true sample, while '1 2 4 5' is not
#the step value between each neighboring element is randomly generated in range(1, 10)

import numpy as np
from ganForTimeSeq import GANForTimeSeq
import os

def removeFileInDir(targetDir): 
    for file in os.listdir(targetDir): 
        targetFile = os.path.join(targetDir,  file) 
        if os.path.isfile(targetFile):
            print ('Delete Old Log FIle:', targetFile)
            os.remove(targetFile)
        elif os.path.isdir(targetFile):
            print ('Delete olds in log dir: ', targetFile)
            removeFileInDir(targetFile)


if __name__ == '__main__':
    n_samples = 10000
    batch_size = 1000
    len_data = 10
    n_iter = 10000
    
    removeFileInDir("tf_writer")

    gndTruthData = (np.ones((n_samples, len_data)) * np.linspace(1, 10, 10)) + 0.05*np.random.randn(n_samples, len_data)
    #gndTruthData = np.random.randn(n_samples, len_data)
    gndTruthData = np.reshape(gndTruthData, [-1, len_data, 1])
    #print gndTruthData[0]
    #noise_data = np.linspace(-1, 1, len_data) + 0.005*np.random.randn(n_samples, len_data)
    noise_data = np.random.uniform(-1, 1, size =(n_samples, len_data))
    g_label_tensor  = np.random.randn(batch_size, len_data)

    gan = GANForTimeSeq(len_data, lr_g=0.01, lr_d=0.001, useGPU=True)
    gan.train(batch_size, n_iter, gndTruthData, None, g_label_tensor)
