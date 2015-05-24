import numpy as np
import matplotlib.pyplot as plt

import pickle

FILENAME = 'tuning.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

    neuron1avg = np.mean(data['neuron1'],axis=0)
    neuron2avg = np.mean(data['neuron2'],axis=0)
    neuron3avg = np.mean(data['neuron3'],axis=0)
    neuron4avg = np.mean(data['neuron4'],axis=0)
    stim = data['stim']

    plt.subplot(2,2,1)
    plt.plot(stim, neuron1avg)

    plt.subplot(2,2,2)
    plt.plot(stim, neuron2avg)

    plt.subplot(2,2,3)
    plt.plot(stim, neuron3avg)

    plt.subplot(2,2,4)
    plt.plot(stim, neuron4avg)

    plt.show()