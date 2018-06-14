import h5py as hp
import numpy as np
import scipy.interpolate as sinp

with hp.File('850mb_300m_10min.hdf5') as loadfile:
 u = loadfile['u'][:]
 v = loadfile['v'][:]
 loadfile.close()

with hp.File('850mb_NAM_gridpoints.hdf5') as loadfile:
 x = loadfile['x'][0,:]
 y = loadfile['y'][:,0]
 t = loadfile['t'][:]
 loadfile.close()
numpts = 16*2*3600+1
twant = np.linspace(46,62,numpts)
theta = np.linspace(0,-np.pi*16*10,numpts)
r = 2000
x0=169.4099
y0=-1043.9
xwant = r*np.cos(theta)+x0
ywant = r*np.sin(theta)+y0
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.close('all')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xwant,ywant,twant)
'''

ufunc = sinp.RegularGridInterpolator(points=[t,y,x],values=u,method='linear')
uwant = ufunc((twant,ywant,xwant))
u=uwant
del ufunc, uwant
vfunc = sinp.RegularGridInterpolator(points=[t,y,x],values=v,method='linear')
vwant = vfunc((twant,ywant,xwant))
v = vwant
t = twant
y = ywant
x = xwant
del vfunc, vwant, xwant, ywant, twant

with hp.File('virtualFlight_r=%04d.hdf5' % r) as savefile:
    savefile.create_dataset('u',shape=u.shape,data=u)
    savefile.create_dataset('v',shape=v.shape,data=v)
    savefile.create_dataset('x',shape=x.shape,data=x)
    savefile.create_dataset('y',shape=y.shape,data=y)
    savefile.create_dataset('t',shape=t.shape,data=t)
    savefile.create_dataset('theta',shape=theta.shape,data=theta)
    savefile.close()