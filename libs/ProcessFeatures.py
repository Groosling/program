__author__ = 'Martin'
import numpy as np
from model.UnprocessedFeatures import UnprocessedFeatures
from model.ProcessedSound import ProcessedSound
from model.Features import Features
import scipy


def mean_of_columns(feat):
    temp = feat.transpose()  # transpose to make coefficients rows
    y, x = temp.shape
    mean = np.array([])
    for i in range(0,y): # for every coeff
        mean = np.append(mean,np.mean(temp[i]))
    return mean

def variance_of_columns(feat):
    temp = feat.transpose()  # transpose to make coefficients rows
    y, x = temp.shape
    variance = np.array([])
    for i in range(0,y): # for every coeff
        variance = np.append(variance,np.var(temp[i]))
    return variance

def min_of_columns(feat):
    temp = feat.transpose()  # transpose to make coefficients rows
    y, x = temp.shape
    min = np.array([])
    for i in range(0,y): # for every coeff
        min = np.append(min, np.amin(temp[i]))
    return min

def max_of_columns(feat):
    temp = feat.transpose()  # transpose to make coefficients rows
    y, x = temp.shape
    max = np.array([])
    for i in range(0,y): # for every coeff
        max = np.append(max, np.amax(temp[i]))
    return max


def compute_mean(unprocessed_feat):

    """
    Compute mean value odf all features - mfcc,lpc ande their deltas are list of size of coefficients
    """
    #MFCC
    mfcc_mean = mean_of_columns(unprocessed_feat.mfcc)
    d_mfcc_mean = mean_of_columns(unprocessed_feat.d_mfcc)

    #LPC
    lpc_mean = mean_of_columns(unprocessed_feat.lpc)
    d_lpc_mean = mean_of_columns(unprocessed_feat.d_lpc)

    #spectral centroid
    spec_centroid_mean =  np.mean(unprocessed_feat.spec_centroid)
    d_spec_centroid_mean =  np.mean(unprocessed_feat.d_spec_centroid)

    #zero-crossing-rate
    zc_rate_mean =  np.mean(unprocessed_feat.zc_rate)
    d_zc_rate_mean =  np.mean(unprocessed_feat.d_zc_rate)

    mean = Features( mfcc_mean, d_mfcc_mean, lpc_mean, d_lpc_mean, zc_rate_mean, d_zc_rate_mean, spec_centroid_mean, d_spec_centroid_mean)
    return mean

def compute_variance(unprocessed_feat):
    """
    Compute standart deviation of all features - mfcc,lpc ande their deltas are list of size of coefficients
    """
    #MFCC
    var_mfcc =  variance_of_columns(unprocessed_feat.mfcc)
    var_d_mfcc = variance_of_columns(unprocessed_feat.d_mfcc)

    #LPC
    var_lpc = variance_of_columns(unprocessed_feat.lpc)
    var_d_lpc = variance_of_columns(unprocessed_feat.d_lpc)

    #zero-crossing rate
    var_zc_rate = np.var(unprocessed_feat.zc_rate)
    var_d_zc_rate = np.var(unprocessed_feat.d_zc_rate)

    #spectral centroid
    var_spec_centroid = np.var(unprocessed_feat.spec_centroid)
    var_d_spec_centroid = np.var(unprocessed_feat.d_spec_centroid)

    variance = Features( var_mfcc, var_d_mfcc, var_lpc, var_d_lpc, var_zc_rate, var_d_zc_rate, var_spec_centroid, var_d_spec_centroid)
    return variance

def compute_min(unprocessed_feat):
    #MFCC
    min_mfcc =  min_of_columns(unprocessed_feat.mfcc)
    min_d_mfcc =  min_of_columns(unprocessed_feat.d_mfcc)

    #LPC
    min_lpc =  min_of_columns(unprocessed_feat.lpc)
    min_d_lpc =  min_of_columns(unprocessed_feat.d_lpc)

    #zero-crossing rate
    min_zc_rate = np.amin(unprocessed_feat.zc_rate)
    min_d_zc_rate = np.amin(unprocessed_feat.d_zc_rate)

    #spectral centroid
    min_spec_centroid = np.amin(unprocessed_feat.spec_centroid)
    min_d_spec_centroid = np.amin(unprocessed_feat.d_spec_centroid)

    min = Features( min_mfcc, min_d_mfcc, min_lpc, min_d_lpc, min_zc_rate, min_d_zc_rate, min_spec_centroid, min_d_spec_centroid)
    return min

def compute_max(unprocessed_feat):
    #MFCC
    max_mfcc =  max_of_columns(unprocessed_feat.mfcc)
    max_d_mfcc =  max_of_columns(unprocessed_feat.d_mfcc)

    #LPC
    max_lpc =  max_of_columns(unprocessed_feat.lpc)
    max_d_lpc =  max_of_columns(unprocessed_feat.d_lpc)

    #zero-crossing rate
    max_zc_rate = np.amax(unprocessed_feat.zc_rate)
    max_d_zc_rate = np.amax(unprocessed_feat.d_zc_rate)

    #spectral centroid
    max_spec_centroid = np.amax(unprocessed_feat.spec_centroid)
    max_d_spec_centroid = np.amax(unprocessed_feat.d_spec_centroid)

    max = Features( max_mfcc, max_d_mfcc, max_lpc, max_d_lpc, max_zc_rate, max_d_zc_rate, max_spec_centroid, max_d_spec_centroid)
    return max


def processFeatures(unprocessed_feat):

    mean =  compute_mean(unprocessed_feat)
    variance = compute_variance(unprocessed_feat)
    min = compute_min(unprocessed_feat)
    max =  compute_max(unprocessed_feat)

    sound = ProcessedSound(mean, variance, min, max,0)
    return sound


    print "TODO"