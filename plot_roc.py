# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 16:46:36 2018

@author: pnola
"""

from cRidge_passing_times import *
import numpy as np
import h5py as hp

rhodot_TPR = []
rhodot_FPR = []
s1_TPR = []
s1_FPR = []

with hp.File('850mb_300m_10min_NAM_Rhodot_Origin_t=0-215hrs_Sept2017.hdf5','r') as data:
    rhodot = data['rhodot'][:].squeeze()
    s1 = data['s1'][:].squeeze()
    t = data['t'][:].squeeze()
    data.close()


a=hr_1_thresh_0()+24
thresh_rhodot = 0
thresh_s1 = 0

rhodot_true_positive = 0
rhodot_false_positive = 0
rhodot_true_negative = 0
rhodot_false_negative = 0
#for tt in range(1267):
for tt in range(24,1291):#1267):
    if len([x for x in a if x == tt])!=0:
        if rhodot[tt]<thresh_rhodot:    
            rhodot_true_positive += 1
        else:
            rhodot_false_negative += 1
    else:
        if rhodot[tt]<thresh_rhodot:    
            rhodot_false_positive += 1
        else:
            rhodot_true_negative += 1

rhodot_total_true = rhodot_true_positive+rhodot_true_negative
rhodot_total_false = rhodot_false_positive+rhodot_false_negative
rhodot_total_positive = rhodot_true_positive+rhodot_false_positive
rhodot_total_negative = rhodot_true_negative+rhodot_false_negative

rhodot_TPR.append(rhodot_true_positive/(rhodot_true_positive+rhodot_false_negative))
rhodot_FPR.append(rhodot_false_positive/(rhodot_false_positive+rhodot_true_negative))


s1_true_positive = 0
s1_false_positive = 0
s1_true_negative = 0
s1_false_negative = 0
#for tt in range(1267):
for tt in range(24,1291):#1267):
    if len([x for x in a if x == tt])!=0:
        if s1[tt]<thresh_s1:    
            s1_true_positive += 1
        else:
            s1_false_negative += 1
    else:
        if s1[tt]<thresh_s1:    
            s1_false_positive += 1
        else:
            s1_true_negative += 1

s1_total_true = s1_true_positive+s1_true_negative
s1_total_false = s1_false_positive+s1_false_negative
s1_total_positive = s1_true_positive+s1_false_positive
s1_total_negative = s1_true_negative+s1_false_negative
s1_TPR.append(s1_true_positive/(s1_true_positive+s1_false_negative))
s1_FPR.append(s1_false_positive/(s1_false_positive+s1_true_negative))

a=hr_1_percentile_50()+24
thresh_rhodot = -np.percentile(-rhodot[rhodot<0],50)
thresh_s1 = -np.percentile(-s1[s1<0],50)

rhodot_true_positive = 0
rhodot_false_positive = 0
rhodot_true_negative = 0
rhodot_false_negative = 0
#for tt in range(1267):
for tt in range(24,1291):#1267):
    if len([x for x in a if x == tt])!=0:
        if rhodot[tt]<thresh_rhodot:    
            rhodot_true_positive += 1
        else:
            rhodot_false_negative += 1
    else:
        if rhodot[tt]<thresh_rhodot:    
            rhodot_false_positive += 1
        else:
            rhodot_true_negative += 1

rhodot_total_true = rhodot_true_positive+rhodot_true_negative
rhodot_total_false = rhodot_false_positive+rhodot_false_negative
rhodot_total_positive = rhodot_true_positive+rhodot_false_positive
rhodot_total_negative = rhodot_true_negative+rhodot_false_negative

rhodot_TPR.append(rhodot_true_positive/(rhodot_true_positive+rhodot_false_negative))
rhodot_FPR.append(rhodot_false_positive/(rhodot_false_positive+rhodot_true_negative))


s1_true_positive = 0
s1_false_positive = 0
s1_true_negative = 0
s1_false_negative = 0
#for tt in range(1267):
for tt in range(24,1291):#1267):
    if len([x for x in a if x == tt])!=0:
        if s1[tt]<thresh_s1:    
            s1_true_positive += 1
        else:
            s1_false_negative += 1
    else:
        if s1[tt]<thresh_s1:    
            s1_false_positive += 1
        else:
            s1_true_negative += 1

s1_total_true = s1_true_positive+s1_true_negative
s1_total_false = s1_false_positive+s1_false_negative
s1_total_positive = s1_true_positive+s1_false_positive
s1_total_negative = s1_true_negative+s1_false_negative
s1_TPR.append(s1_true_positive/(s1_true_positive+s1_false_negative))
s1_FPR.append(s1_false_positive/(s1_false_positive+s1_true_negative))


a=hr_1_percentile_90()+24
thresh_rhodot = -np.percentile(-rhodot[rhodot<0],90)
thresh_s1 = -np.percentile(-s1[s1<0],90)

rhodot_true_positive = 0
rhodot_false_positive = 0
rhodot_true_negative = 0
rhodot_false_negative = 0
#for tt in range(1267):
for tt in range(24,1291):#1267):
    if len([x for x in a if x == tt])!=0:
        if rhodot[tt]<thresh_rhodot:    
            rhodot_true_positive += 1
        else:
            rhodot_false_negative += 1
    else:
        if rhodot[tt]<thresh_rhodot:    
            rhodot_false_positive += 1
        else:
            rhodot_true_negative += 1

rhodot_total_true = rhodot_true_positive+rhodot_true_negative
rhodot_total_false = rhodot_false_positive+rhodot_false_negative
rhodot_total_positive = rhodot_true_positive+rhodot_false_positive
rhodot_total_negative = rhodot_true_negative+rhodot_false_negative

rhodot_TPR.append(rhodot_true_positive/(rhodot_true_positive+rhodot_false_negative))
rhodot_FPR.append(rhodot_false_positive/(rhodot_false_positive+rhodot_true_negative))


s1_true_positive = 0
s1_false_positive = 0
s1_true_negative = 0
s1_false_negative = 0
#for tt in range(1267):
for tt in range(24,1291):#1267):
    if len([x for x in a if x == tt])!=0:
        if s1[tt]<thresh_s1:    
            s1_true_positive += 1
        else:
            s1_false_negative += 1
    else:
        if s1[tt]<thresh_s1:    
            s1_false_positive += 1
        else:
            s1_true_negative += 1

s1_total_true = s1_true_positive+s1_true_negative
s1_total_false = s1_false_positive+s1_false_negative
s1_total_positive = s1_true_positive+s1_false_positive
s1_total_negative = s1_true_negative+s1_false_negative
s1_TPR.append(s1_true_positive/(s1_true_positive+s1_false_negative))
s1_FPR.append(s1_false_positive/(s1_false_positive+s1_true_negative))


import matplotlib.pyplot as plt
plt.close('all')
plt.figure(1)
plt.plot([0,1],[0,1],'b--')
plt.plot(rhodot_FPR,rhodot_TPR,'r')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Rhodot')

plt.figure(2)
plt.plot([0,1],[0,1],'b--')
plt.plot(s1_FPR,s1_TPR,'r')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('s1')

plt.figure(3)
plt.plot(s1,'b--')
plt.plot(rhodot,'r')
for x in a:
    plt.axvline(x,alpha=0.3)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('s1')

plt.figure(4)
plt.plot(s1,'b--')
plt.plot(rhodot,'r')
for x in a:
    plt.axvline(x-24,alpha=0.3)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('s1')
