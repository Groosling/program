__author__ = 'Martin'

from libs import ExtractFeatures as feat
from libs import ProcessFeatures as feat2
from model.UnprocessedFeatures import UnprocessedFeatures
import numpy as np
import csv

def save_as_csv(matrix):
    with open("list.csv", "wb") as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerows([matrix])
        f.close()

def  get_list_features(feature):
    """
    Transfrom  feature  atributes and lists to one array
    :param feature: one feature of sounf
    :return: list of feature atributes
    """
    result = np.array([])
    result = np.append(result,feature.mfcc)
    result = np.append(result,feature.d_mfcc)
    result = np.append(result,feature.lpc)
    result = np.append(result,feature.d_lpc)
    result = np.append(result,feature.zc_rate)
    result = np.append(result,feature.d_zc_rate)
    result = np.append(result,feature.spec_centroid)
    result = np.append(result,feature.d_spec_centroid)
    return result


def sound_to_row(sound):
    list = []

    list.append(sound.mean)
    list.append(sound.variance)
    """zatial iba mean a variance"""
   # list.append(sound.min)
   # list.append(sound.max)

    result = np.array([])
    result = np.append(result,sound.category)
    for feat in list:

        result = np.append(result, get_list_features(feat))
    return result

def save(list_of_sounds):
    rows = []
    #titles = np.array([])
    # category, 13x mean_mfcc,13x mean_d_mfcc, 12x mean_lpc, 12x mean_d_lpc, zc_rate,d_zc_rate, spec_centroid, d_spec_centroid
    # to iste pre deviatiom
    # titles=np.append(titles,["Category","mean_mfcc0","mean_mfcc1","mean_mfcc2","mean_mfcc3","mean_mfcc4","mean_mfcc5",
    #                 "mean_mfcc6","mean_mfcc7","mean_mfcc8","mean_mfcc9","mean_mfcc10","mean_mfcc11","mean_mfcc12",
    #                 "mean_d_mfcc0","mean_d_mfcc1","mean_d_mfcc2","mean_d_mfcc3","mean_d_mfcc4","mean_d_mfcc5",
    #                 "mean_d_mfcc6","mean_d_mfcc7","mean_d_mfcc8","mean_d_mfcc9","mean_d_mfcc10","mean_d_mfcc11",
    #                 "mean_d_mfcc12","mean_lpc0","mean_lpc1","mean_lpc2","mean_lpc3","mean_lpc4","mean_lpc5",
    #                 "mean_lpc6","mean_lpc7","mean_lpc8","mean_lpc9","mean_lpc10","mean_lpc11","mean_d_lpc0",
    #                 "mean_d_lpc1","mean_d_lpc2","mean_d_lpc3","mean_d_lpc4","mean_d_lpc5","mean_d_lpc6","mean_d_lpc7",
    #                 "mean_d_lpc8","mean_d_lpc9","mean_d_lpc10","mean_d_lpc11","mean_zc_rate","mean_d_zc_rate",
    #                 "mean_spec_centroid","mean_d_spec_centroid",
    #                 "dev_mfcc0","dev_mfcc1","dev_mfcc2","dev_mfcc3","dev_mfcc4","dev_mfcc5",
    #                 "dev_mfcc6","dev_mfcc7","dev_mfcc8","dev_mfcc9","dev_mfcc10","dev_mfcc11","dev_mfcc12",
    #                 "dev_d_mfcc0","dev_d_mfcc1","dev_d_mfcc2","dev_d_mfcc3","dev_d_mfcc4","dev_d_mfcc5",
    #                 "dev_d_mfcc6","dev_d_mfcc7","dev_d_mfcc8","dev_d_mfcc9","dev_d_mfcc10","dev_d_mfcc11",
    #                 "dev_d_mfcc12","dev_lpc0","dev_lpc1","dev_lpc2","dev_lpc3","dev_lpc4","dev_lpc5",
    #                 "dev_lpc6","dev_lpc7","dev_lpc8","dev_lpc9","dev_lpc10","dev_lpc11","dev_d_lpc0",
    #                 "dev_d_lpc1","dev_d_lpc2","dev_d_lpc3","dev_d_lpc4","dev_d_lpc5","dev_d_lpc6","dev_d_lpc7",
    #                 "dev_d_lpc8","dev_d_lpc9","dev_d_lpc10","dev_d_lpc11","dev_zc_rate","dev_d_zc_rate",
    #                 "dev_spec_centroid","dev_d_spec_centroid"
    #                 ])
    # rows.append(titles)
    for sound in list_of_sounds:
        rows.append(sound_to_row(sound))
#    save_as_csv(rows)
    np.savetxt("list.csv", rows, delimiter=",")
    print "daco"


def extractFeatures(signal, fs=44100):

    # Secondary features signal
    trans_signal = feat.transform_signal(signal)

    #MFCC
    mfcc = feat.mfcc_coeff(signal,fs)
    d_mfcc = feat.mfcc_coeff(trans_signal,fs)

    #LPC
    lpc = feat.lpc_coeff(signal)
    d_lpc = feat.lpc_coeff(trans_signal)


    #Spectral centroid
    spec_centroid = feat.spec_centroid(signal,fs)
    d_spec_centroid = feat.spec_centroid(trans_signal,fs)

    #zero-crossing rate
    zc_rate = feat.zc_rate(signal,fs)
    d_zc_rate =  feat.zc_rate(trans_signal,fs)

    # save all as one object
    unprocessed_feat =  UnprocessedFeatures(mfcc,d_mfcc,lpc,d_lpc,zc_rate,d_zc_rate,spec_centroid,d_spec_centroid)

    #process more....
    sound = feat2.processFeatures(unprocessed_feat)
   # save(sound)
    return sound

def process_sounds(list_of_signals,list_of_categories,fs=44100):
    list_of_sounds = []
    i=0
    for sound in list_of_signals:
        list_of_sounds.append(extractFeatures(sound))
        list_of_sounds[i].category = list_of_categories[i]
        i+=1
    save(list_of_sounds)
    print "Koniec"