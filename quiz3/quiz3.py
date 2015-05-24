import numpy as np
import matplotlib.pyplot as plt

import pickle

FILENAME = 'tuning.pickle'

def plot_tuning_curves(data):
    stim = data['stim']

    for i in range(4):
        idx = i + 1

        neuron_avg = np.mean(data['neuron%s' % str(idx)],axis=0)

        plt.subplot(2,2,idx)
        plt.plot(stim, neuron_avg)

    plt.show()

def non_poisson(data):
    for i in range(4):
        idx = i + 1

        neuron_avg = np.mean(data['neuron%s' % str(idx)],axis=0)
        neuron_std = np.std(data['neuron%s' % str(idx)],axis=0)

        plt.subplot(2,2,idx)
        plt.plot(neuron_std**2, neuron_avg)
    plt.show()

def main():
    with open(FILENAME, 'rb') as f:
        data = pickle.load(f)
        plot_tuning_curves(data)
        non_poisson(data)

if __name__ == '__main__':
    main()