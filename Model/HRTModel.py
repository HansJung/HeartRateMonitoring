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
    RecordNum = '00735'
    # AF : 201, 202, 203

    FilePath = "../Data/MITBIH_AF/"+ str(RecordNum) + ".txt"
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
    EpisodeLabel = list()

    for a in File.readlines():
        A = a.split(" ")
        A = [a for a in A if a != '']
        LastElem =  A[-1]
        LastElem = LastElem.replace("\n","")
        LastElem = LastElem.replace('\t','')
        LastElem = LastElem.replace('0','')
        if LastElem == '':
            EpisodeLabel.append(EpisodeLabel[-1])
        else:
            LastElem = LastElem.replace('(','')
            LastElem = LastElem.replace(')','')
            EpisodeLabel.append(LastElem)
        if idx > 0:
            time = A[0]
            rIdx = A[1]
            beatLabel  = A[2]
            time = time.replace('[','')
            time = time.replace(']','')
            # print time
            Sec = getSec_Arr(time)

            Time.append(Sec)
            RIdx.append(rIdx)
            BeatLabel.append(beatLabel)

        idx += 1

    Time = np.array(Time)
    RR = Time[1:] - Time[:-1]


    plt.figure()
    plt.title(RecordNum)
    for idx in range(len(RR)):
        rr = RR[idx]
        current_Beat = BeatLabel[idx+1]
        rIdx = RIdx[idx+1]
        CurrentTime = Time[idx]
        episodeLabel = EpisodeLabel[idx]

        print rIdx, CurrentTime, rr, current_Beat, episodeLabel

        if episodeLabel == 'N':
            plt.plot(rIdx, rr, 'bo')
        elif episodeLabel == "AFIB":
            plt.plot(rIdx, rr, 'ro')
        else:
            plt.plot(rIdx, rr, 'go')

    rrSum = 0
    # plt.figure()
    # for idx in range(len(RR)):
    #     rIdx = RIdx[idx+1]
    #     rr = RR[idx]
    #     rrSum += rr
    #     plt.plot(idx, rrSum,'bo')

    plt.show()













