__author__ = 'Martin'
from scikits import audiolab
from scikits.talkbox.features import mfcc
import matplotlib.pyplot as plt
import time
import numpy as np
from scikits.talkbox import lpc
import scipy

# ----------- Helpful functions -----------------------------

def transform_signal(sig, D = 5):
    """
    y(t)' =  y(t+D) - y(t), 1 <= t <= n-D
    :param sig: signal for transformation
    :param D: distance of compared data points
    :return: transformed signal
    """
    signal = sig[D:] - sig[:-D]
    return signal


def delta_of_matrix(features):
    """
    Method that compute deltas of values in columns = in most cases delta of coefficient in time
    :param features: matrix of features
    :return: np.array
    """
    y, x = features.shape
    delta_features = []

    for i in range(0,y-1):
        newrow =features[i][:] -features[i+1][:]
        delta_features.append(newrow)

    delta_features= np.array(delta_features)

    return delta_features

def delta_of_array(array):
    """
    Compute deltas of values in 1D np.array
    :param array: np.array of features
    :return: 1D list of deltas of features
    """

    delta_features = np.array([])
    for i in range(0,(array.size)-1):
     delta_features=np.append(delta_features,(array[i] - array[i+1]))
    return delta_features


def reshapeSignal(sig, size=512):
    """
    Reshape signal to matrix of shape (n/size,size)
    :param sig: signal to reshape
    :param size: size of window
    :return: reshaped signal
    """
    leng = 512 - (len(sig)%size) #how many array cell are missing
    signal = np.array([sig])
    signal = np.append(signal, np.zeros(leng)) # add missing cells
    num_of_rows = signal.size/size
    signal = np.reshape(signal,(num_of_rows,size))
    signal = signal[~np.all(signal == 0, axis=1)] # delete zero rows
    return signal


def spectral_centroid(x, samplerate=44100):
    """
    Compute frequency of center energy of window
    :param x: signal
    :param samplerate: number of samples per second
    :return: frequency of center energy
    """
    magnitudes = np.abs(np.fft.rfft(x)) # magnitudes of positive frequencies
    length = x.size
    freqs = np.abs(np.fft.fftfreq(length, 1.0/samplerate)[:length//2+1]) # positive frequencies
    return np.sum(magnitudes*freqs) / np.sum(magnitudes) # return weighted mean

def spectralCentroidWholeSound(signal, rate):
    """
    Compute spectral centroid of whole sound
    :param signal: reshaped signal
    :param rate: samples per second
    :return: np.array of spectral centroids
    """
    spec_cetroid = np.array([])
    num_of_rows, x = signal.shape
    for i in range(0,num_of_rows):
        spec_cetroid = np.append(spec_cetroid,spectral_centroid(signal[i],rate))
    return spec_cetroid

def number_of_zeroCrossing(x, sampleRate=44100):
   temp = scipy.where(x[:-1] * x[1:] < 0)
   temp2 = np.array([temp[0]])
   return temp2[0].size # [0] there was many arrays in arrays

def zcRateOfWholeSignal(signal, rate):
    """
    Compute zero crossing rate of whole sound
    :param signal: reshaped signal
    :param rate: samples per second
    :return: np.array of zero-crossing rate
    """
    features = np.array([])
    num_of_rows, x = signal.shape
    for i in range(0,num_of_rows):
        features = np.append(features,number_of_zeroCrossing(signal[i],rate))
    return features

# ----------- FEATURES -----------------------------
# Zle featry - boli vypocitavane nad vypocitavanymi koeficientami a nie transformovanym signalom
# def d_mfcc2(ceps):
#
#     """ return ndarray"""
#     delta =  delta_of_matrix(ceps)
#     return delta
#
# def d_lpc2(coeff):
#     """ return ndarray"""
#     delta =  delta_of_matrix(coeff)
#     return delta
#
# def d_spec_centroid2(spec_centroid):
#     """ return ndarray """
#     delta = delta_of_array(spec_centroid)
#     return delta
#
#
# def d_zc_rate2(zeroCross):
#     """ return ndarray """
#     delta = delta_of_array(zeroCross)
#     return delta

def mfcc_coeff(signal, fs=44100):
    """ return ndarray"""
    ceps, mspec, spec = mfcc(signal, nwin=256, nfft=512, fs=44100, nceps=13)
    return ceps


def lpc_coeff(sig):
    """ return ndarray"""
    signal = reshapeSignal(sig)
    A, e, k = lpc(signal, 12) # 12 coefficients (n/sizeof window) *k coefficients
    return k

def spec_centroid(sig,fs = 44100):
    """ return ndarray """
    signal = reshapeSignal(sig)
    spec_centroid =spectralCentroidWholeSound(signal,fs)
    return spec_centroid


def zc_rate(sig, fs = 44100):
    """ return ndarray """
    signal = reshapeSignal(sig)
    zeroCross = zcRateOfWholeSignal(signal,fs)
    return zeroCross

