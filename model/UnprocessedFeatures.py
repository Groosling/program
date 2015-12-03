__author__ = 'Martin'
class UnprocessedFeatures(object):

     def __init__(self, mfcc, d_mfcc, lpc, d_lpc, zc_rate,d_zc_rate,spec_centroid,d_spec_centroid):
        self.mfcc = mfcc
        self.d_mfcc = d_mfcc
        self.lpc = lpc
        self.d_lpc = d_lpc
        self.zc_rate = zc_rate
        self.d_zc_rate = d_zc_rate
        self.spec_centroid = spec_centroid
        self.d_spec_centroid =  d_spec_centroid



