# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:59:06 2018

@author: pnola
"""
import matplotlib.pyplot as plt
plt.close('all')
from mpl_toolkits.basemap import Basemap
import os.path
import numpy as np
import h5py as hp
star = [37.19838, -80.57834]
xlen = 259
ylen = 257
tlen = 1267

integration = '-1'
dim = [tlen,ylen,xlen]
origin = [37.208, -80.5803]
print("Begin Map")
m = Basemap(width=77700,height=76800,\
    rsphere=(6378137.00,6356752.3142),\
    resolution='c',area_thresh=0.,projection='lcc',\
    lat_1=35.,lat_0=origin[0],lon_0=origin[1])#,ax=ax)

with hp.File('850mb_300m_10min_NAM_FTLE_Origin_t=4-215hrs_Sept2017_int='+integration+'.hdf5','r') as data:
    ftle1 = data['ftle'][:].squeeze()
    data.close()

with hp.File('850mb_300m_10min_NAM_LCS_t=4-215hrs_Sept2017_int='+integration+'.hdf5','r') as loadfile:
    ftle=loadfile['ftle'][:]
    dirdiv=loadfile['directionalderivative'][:]
    concav=loadfile['concavity'][:]
    loadfile.close()

dirdiv= np.ma.masked_where(concav>0,dirdiv)

x = np.linspace(0, m.urcrnrx, dim[2])
y = np.linspace(0, m.urcrnry, dim[1])
xx, yy = np.meshgrid(x, y)
x, y = m(star[1],star[0])
for radius in [5000,7500]:#[400,800,1200,1600,2000,3000,5000,7500,10000]:#[200,500,800,1000,2000,3500,5000,7500,10000]:#[200,300,400]:#np.linspace(100,10000,37):#[1,10,100,500,1000,5000,10000,15000]:#radius=1000
    for percent in np.arange(0,101,1):
        filename = 'passing_files/passing_times_{0:03d}th_percentile_radius={1:05d}_int='.format(percent,int(radius))+integration+'.npy'
        if not os.path.isfile(filename):
            #print(filename+' exits.')
            #continue
            print(filename)
            thresh=np.percentile(ftle1[ftle1>0],percent,axis=None)
            dirdiv_plot = np.ma.masked_where(ftle<=thresh,dirdiv) 
            passing_times = []
            for t in range(dirdiv.shape[0]):
                #print('{0}th percentile, @ t = {1:04d}'.format(percent,t))
                ridge = m.contour(xx,yy,dirdiv_plot[t,:,:],levels =[0])#,latlon=True)
                pp = ridge.collections[0].get_paths()
                for p in range(len(pp)):
                    v=pp[p].vertices
                    if any((v[:,0]-x)**2+(v[:,1]-y)**2<radius**2):
                        #print('hit @ {0}'.format(t))
                        passing_times.append(t)
                        break
                del ridge, pp
            del dirdiv_plot
            plt.close('all')
            np.save(filename,passing_times)
            



        