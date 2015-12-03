__author__ = 'Martin'
from Features import Features

class ProcessedSound:

     def __init__(self,mean, variance, min, max, category):
        self.category = category
        self.mean = mean
        self.variance = variance
        self.min = min
        self.max = max
