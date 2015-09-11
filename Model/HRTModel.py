# -*- coding: utf-8 -*-
'''
Goal : 
Author : Yonghan Jung, ISyE, KAIST 
Date : 150910
Comment 
- 

'''

''' Library '''
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


''' Function or Class '''


class Example:
    def __init__(self):
        return None

def getSec_Arr(s):
    l = s.split(':')
    Minute = int(l[0])
    a = l[1].split('.')
    Sec = int(a[0])
    MiSec = int(a[1]) * 0.001
    return 60 * Minute + Sec + MiSec

def getSec_Rest(s):
    l = s.split(':')
    Hour = int(l[0])
    Minute = int(l[1])
    a = l[2].split('.')
    Sec = int(a[0])
    MiSec = int(a[1]) * 0.001
    return 3600 * Hour + 60 * Minute + Sec + MiSec


if __name__ == "__main__":
    # Read data
    RecordNum = '16272'
    FilePath = "../Data/MITBIH_Normal/"+ str(RecordNum) + ".txt"
    File = open(FilePath, 'rb')

    Dict_HRV = dict()
    Dict_HRV['Time'] = list()
    Dict_HRV['Sample'] = list()
    Dict_HRV['Type'] = list()
    Dict_HRV['Episode'] = list()

    idx = 0
    Time = list()
    RIdx = list()
    BeatLabel = list()
    for a in File.readlines():
        A = a.split(" ")
        A = [a for a in A if a != '']
        if idx > 0:
            time = A[0]
            rIdx = A[1]
            beatLabel  = A[2]
            time = time.replace('[','')
            time = time.replace(']','')
            # print time
            Sec = getSec_Rest(time)

            Time.append(Sec)
            RIdx.append(rIdx)
            BeatLabel.append(beatLabel)

        idx += 1
        if idx > 1000:
            break
    Time = np.array(Time)
    RR = Time[1:] - Time[:-1]

    for idx in range(len(RR)):
        rr = RR[idx]
        current_Beat = BeatLabel[idx+1]
        rIdx = RIdx[idx+1]
        CurrentTime = Time[idx]

        print rIdx, CurrentTime, rr, current_Beat

        if current_Beat == 'V' or current_Beat == 'r':
            plt.plot(rIdx, rr, 'ro')
        else:
            plt.plot(rIdx, rr, 'bo')

    plt.show()













