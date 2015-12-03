__author__ = 'Martin'
from controll import TrainExtract
from scikits import audiolab
import time


start =  time.time()

list_od_signals = []
list_of_categories = []
""" 1.Class rooster -----------------------------------------------------------"""
""" 2.Class clapping ---------------------------------------------------------------"""
""" 3.Class brushing teeth ---------------------------------------------------------------"""
""" 4.Class dog ---------------------------------------------------------------"""
""" 5.Class cow ---------------------------------------------------------------"""
""" 6.Class water drops ---------------------------------------------------------------"""

"""1.-----------------------------------------------------------"""
[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\rooster\\1-26806-A.wav')
list_od_signals.append(signal)
list_of_categories.append(1)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\clapping\\1-104089-A.wav')
list_od_signals.append(signal)
list_of_categories.append(2)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\brushing_teeth\\1-61534-A.wav')
list_od_signals.append(signal)
list_of_categories.append(3)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\dog\\1-110389-A.wav')
list_od_signals.append(signal)
list_of_categories.append(4)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\cow\\1-16568-A.wav')
list_od_signals.append(signal)
list_of_categories.append(5)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\water_drops\\1-16746-A.wav')
list_od_signals.append(signal)
list_of_categories.append(6)

"""2. ---------------------------------------------------------------"""
[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\rooster\\2-71162-A.wav')
list_od_signals.append(signal)
list_of_categories.append(1)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\clapping\\2-57733-A.wav')
list_od_signals.append(signal)
list_of_categories.append(2)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\brushing_teeth\\2-83536-A.wav')
list_od_signals.append(signal)
list_of_categories.append(3)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\dog\\2-114587-A.wav')
list_od_signals.append(signal)
list_of_categories.append(4)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\cow\\2-103426-A.wav')
list_od_signals.append(signal)
list_of_categories.append(5)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\water_drops\\2-139748-A.wav')
list_od_signals.append(signal)
list_of_categories.append(6)

"""3.---------------------------------------------------------------"""

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\rooster\\2-96460-A.wav')
list_od_signals.append(signal)
list_of_categories.append(1)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\clapping\\2-76408-B.wav')
list_od_signals.append(signal)
list_of_categories.append(2)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\brushing_teeth\\2-92627-A.wav')
list_od_signals.append(signal)
list_of_categories.append(3)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\dog\\2-118072-A.wav')
list_od_signals.append(signal)
list_of_categories.append(4)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\cow\\2-104877-A.wav')
list_od_signals.append(signal)
list_of_categories.append(5)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\water_drops\\2-68595-A.wav')
list_od_signals.append(signal)
list_of_categories.append(6)


"""4.---------------------------------------------------------------"""
[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\rooster\\3-107219-A.wav')
list_od_signals.append(signal)
list_of_categories.append(1)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\clapping\\3-149465-A.wav')
list_od_signals.append(signal)
list_of_categories.append(2)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\brushing_teeth\\3-118069-A.wav')
list_od_signals.append(signal)
list_of_categories.append(3)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\dog\\3-155312-A.wav')
list_od_signals.append(signal)
list_of_categories.append(4)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\cow\\3-124376-B.wav')
list_od_signals.append(signal)
list_of_categories.append(5)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\water_drops\\3-164592-A.wav')
list_od_signals.append(signal)
list_of_categories.append(6)

"""5.---------------------------------------------------------------"""
[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\rooster\\3-137152-A.wav')
list_od_signals.append(signal)
list_of_categories.append(1)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\clapping\\3-177083-A.wav')
list_od_signals.append(signal)
list_of_categories.append(2)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\brushing_teeth\\3-126391-B.wav')
list_od_signals.append(signal)
list_of_categories.append(3)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\dog\\3-170015-A.wav')
list_od_signals.append(signal)
list_of_categories.append(4)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\cow\\3-152039-A.wav')
list_od_signals.append(signal)
list_of_categories.append(5)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\water_drops\\3-164595-A.wav')
list_od_signals.append(signal)
list_of_categories.append(6)


""" 6.---------------------------------------------------------------"""

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\rooster\\3-149189-A.wav')
list_od_signals.append(signal)
list_of_categories.append(1)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\clapping\\3-197435-B.wav')
list_od_signals.append(signal)
list_of_categories.append(2)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\brushing_teeth\\3-139331-A.wav')
list_od_signals.append(signal)
list_of_categories.append(3)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\dog\\3-180977-A.wav')
list_od_signals.append(signal)
list_of_categories.append(4)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\cow\\3-163727-A.wav')
list_od_signals.append(signal)
list_of_categories.append(5)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\water_drops\\3-166326-A.wav')
list_od_signals.append(signal)
list_of_categories.append(6)

""" 7.---------------------------------------------------------------"""

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\rooster\\4-164021-A.wav')
list_od_signals.append(signal)
list_of_categories.append(1)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\clapping\\4-189828-A.wav')
list_od_signals.append(signal)
list_of_categories.append(2)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\brushing_teeth\\4-144468-A.wav')
list_od_signals.append(signal)
list_of_categories.append(3)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\dog\\4-182395-A.wav')
list_od_signals.append(signal)
list_of_categories.append(4)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\cow\\4-174860-A.wav')
list_od_signals.append(signal)
list_of_categories.append(5)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\water_drops\\4-168155-A.wav')
list_od_signals.append(signal)
list_of_categories.append(6)

""" 8.---------------------------------------------------------------"""

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\rooster\\4-164064-A.wav')
list_od_signals.append(signal)
list_of_categories.append(1)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\clapping\\4-189830-A.wav')
list_od_signals.append(signal)
list_of_categories.append(2)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\brushing_teeth\\4-144468-B.wav')
list_od_signals.append(signal)
list_of_categories.append(3)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\dog\\4-183992-A.wav')
list_od_signals.append(signal)
list_of_categories.append(4)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\cow\\4-174860-B.wav')
list_od_signals.append(signal)
list_of_categories.append(5)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\water_drops\\4-174797-A.wav')
list_od_signals.append(signal)
list_of_categories.append(6)




""" 9.---------------------------------------------------------------"""

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\rooster\\5-194930-A.wav')
list_od_signals.append(signal)
list_of_categories.append(1)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\clapping\\5-209989-A.wav')
list_od_signals.append(signal)
list_of_categories.append(2)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\brushing_teeth\\5-147297-A.wav')
list_od_signals.append(signal)
list_of_categories.append(3)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\dog\\5-203128-A.wav')
list_od_signals.append(signal)
list_of_categories.append(4)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\cow\\5-194899-A.wav')
list_od_signals.append(signal)
list_of_categories.append(5)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\water_drops\\5-241846-A.wav')
list_od_signals.append(signal)
list_of_categories.append(6)

""" 10.---------------------------------------------------------------"""

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\rooster\\5-194930-B.wav')
list_od_signals.append(signal)
list_of_categories.append(1)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\clapping\\5-218494-A.wav')
list_od_signals.append(signal)
list_of_categories.append(2)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\brushing_teeth\\5-180229-A.wav')
list_od_signals.append(signal)
list_of_categories.append(3)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\dog\\5-203128-B.wav')
list_od_signals.append(signal)
list_of_categories.append(4)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\cow\\5-194899-B.wav')
list_od_signals.append(signal)
list_of_categories.append(5)

[signal, fs, nbBits] = audiolab.wavread('D:\\datasety\\water_drops\\5-254832-A.wav')
list_od_signals.append(signal)
list_of_categories.append(6)

TrainExtract.process_sounds(list_od_signals,list_of_categories, fs)

end =  time.time()

print "Cas vykonania:",end-start,"s"