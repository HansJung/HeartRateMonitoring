# -*- coding: utf-8 -*-
'''
Goal : 
Author : Yonghan Jung, ISyE, KAIST 
Date : 15
Comment 
- 

'''

''' Library '''
import numpy as np
import matplotlib.pyplot as plt
''' Function or Class '''


class Example:
    def __init__(self):
        return None

def ReaderSetting(row):
    ListRow = row.split(" ")
    ListRow = [x for x in ListRow if x != '']
    # Time
    TimeElem = ListRow[0]
    TimeElem = TimeElem.replace('[','')
    TimeElem = TimeElem.replace(']','')
    # print TimeElem
    TimeNum = GetSec_Mode1(TimeElem)

    # rIdx
    rIdx = int(ListRow[1])

    # BeatLabel
    BeatLabel = ListRow[2].replace(" ", '')

    # EpisodeLabel
    EpisodeLabel = ListRow[-1]
    EpisodeLabel = EpisodeLabel.replace('\n','')
    if EpisodeLabel == '0':
        EpisodeLabel = '0'
    else:
        EpisodeLabel = EpisodeLabel.replace('(','')
        EpisodeLabel = EpisodeLabel.replace(')','')

    return [TimeNum, rIdx, BeatLabel, EpisodeLabel]

def GetSec_Mode1(TimeElem):
    ListTimeElem = TimeElem.split(":")
    Hour = int(ListTimeElem[0]) * 3600
    Minute = int(ListTimeElem[1]) * 60
    Seconds = int(ListTimeElem[2].split(".")[0])
    MinSeconds = int(ListTimeElem[2].split(".")[1]) * 0.001

    return Hour + Minute + Seconds + MinSeconds




if __name__ == "__main__":
    RecordName = '04048'
    File = RecordName + '.txt'
    ReadFile = open(File,'rb')

    IterIdx = 0
    RTime = list()
    RIdx = list()
    BeatLabel = list()
    EpiLabel = list()
    FinalData = list()
    for row in ReadFile:
        if IterIdx > 0 :
            InfoRow = ReaderSetting(row)
            RTime.append(InfoRow[0])
            RIdx.append(InfoRow[1])
            BeatLabel.append(InfoRow[2])
            # EpiLabel.append(InfoRow[3])
            if InfoRow[-1] == '0':
                EpiLabel.append(EpiLabel[-1])
            else:
                EpiLabel.append(InfoRow[3])
            FinalData.append([RTime[-1], RIdx[-1], BeatLabel[-1], EpiLabel[-1]])
        IterIdx += 1

    RRInterval = np.array(RTime[1:]) - np.array(RTime[:-1])
    RIdx = RIdx[1:]
    BeatLabel = BeatLabel[1:]
    EpiLabel = EpiLabel[1:]

    for idx in range(len(RRInterval)):
        if EpiLabel[idx] == 'N':
            plt.plot(idx, RRInterval[idx],'bo')
        elif EpiLabel[idx] == 'AFIB':
            plt.plot(idx, RRInterval[idx],'ro')
        else:
            plt.plot(idx, RRInterval[idx],'go')

    plt.show()
