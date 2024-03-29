''' OpenBCI Simulator '''

''' EXAMPLE: '''

'''
def handle_sample(sample):
    print(sample.channel_data)
CHANNELS = [1,2,3,4]
board_sim = OpenBCISimulator("/home/.../.../SUBJ1/SSVEP_8Hz_Trial3_SUBJ1.csv",
CHANNELS)
board_sim.start_streaming(handle_sample)
'''

import time
import numpy as np

class OpenBCISimulator(object):
    """OpenBCI Ganglion simulator class. Generate sample object from eeg file,
    and pass it further by callback function.
    Parameters
    ----------
    path : string
        Path of your eeg data set. e.g "/home/SUBJ1/SSVEP_8Hz_Trial3_SUBJ1.csv"
    channels : list
        Selected channels for generator. Min. 1 Max. 4 channels.
    sample_rate : integer
        Sampling rate, default for Ganglion 250.
    test : boolean
        If true, all samples will be parse instantly, without simulating
        sample rate time.
    """

    def __init__(self, channels, sample_rate=250, subj=0,
                 path = '../BakSys/data/SUBJ1/SSVEP_14Hz_Trial1_SUBJ1.csv',
                 delimiter = ','):
        self.sample_rate = sample_rate
        self.channels = channels
        self.subj = subj
        self.path = path
        self.data = np.loadtxt(self.path,delimiter=delimiter)[:, self.channels]

    def start_streaming(self, callback):

        """
        Strams the data from given file, simulating OpenBCI
        """

        __temp = []
        for i in range(len(self.data)):
            for j in self.data[i]:
                __temp.append(j)
            sample = OpenBCISample(i, __temp)
            __temp = []
            #if not self.test:
            #    time.sleep(1./self.sample_rate)
            callback(sample)


class OpenBCISample(object):
    """Object encapulsating a single sample from the OpenBCI board."""
    def __init__(self, packet_id, channel_data):
        self.id = packet_id
        self.channel_data = channel_data

def print_sample(sample):
    print(sample.channel_data)

if __name__ == "__main__":
    bci = OpenBCISimulator([0,1])
    bci.start_streaming(print_sample)
