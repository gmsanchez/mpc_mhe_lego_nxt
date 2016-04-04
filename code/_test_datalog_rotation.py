import numpy as np
import time
import matplotlib.pyplot as plt
import sys

from nxt_lib.nxt_list import nxt_list, data_idx
from nxt_lib.utils import DataLogger
import nxt_lib.brick as brick

def get_velocities(_t):
    _vl = 0.0
    _vr = 0.0
    if _t<1.0:
        _vl = 0.0
        _vr = 0.0
    if _t>=1.0 and _t<3.0:
        _vl = 50.0*(_t-1.0)
        _vr = _vl
    if _t>=3.0 and _t<6.0:
        _vl = 100.0
        _vr = 100.0
    if _t>=6.0 and _t<8.0:
        _vl = -50.0*(_t-6.0)+100.0
        _vr = _vl
    if _t>=8.0:
        _vl = 0.0
        _vr = 0.0
    return (_vl, _vr)

def get_velocities_01(_t):
    _vl = 0.0
    _vr = 0.0
    if _t<2.0:
        _vl = 0.0
        _vr = 0.0
    if _t>=2.0 and _t<6.0:
        _vl = 30.0
        _vr = 30.0
    if _t>=6.0 and _t<8.0:
        _vl = 0.0
        _vr = 0.0
    if _t>=8.0 and _t<12.0:
        _vl = -30.0
        _vr = -30.0
    if _t>=12.0:
        _vl = 0.0
        _vr = 0.0
    return (_vl, _vr)



Ts = 250E-3 # en segundos
logging_time = 14 # segundos
NUM_SAMPLES = logging_time/Ts
DATA_SIZE = len(data_idx)


t = np.arange(0, logging_time,Ts)
vl = np.zeros(NUM_SAMPLES)
vr = np.zeros(NUM_SAMPLES)
for j,k in enumerate(t):
    (vl[j], vr[j]) = get_velocities(k)

d03 = DataLogger(NUM_SAMPLES, DATA_SIZE)
nxt03 = nxt_list["03"]
b03 = brick.Brick(nxt03["name"], nxt03["mac"], nxt03["port"])
b03.connect()

do_loop = True
k = 0

if b03.sock.connected:
     raw_input("Press enter to continue...")
     while do_loop:
         tk = t[k]
         (vlk, vrk) = get_velocities_01(tk)
         if k == NUM_SAMPLES-1:
             do_loop = False
             
         
         data03 = b03.recv_data()
         if data03:
             d03.update(np.asarray(data03))
             b03.send_motor_power(vlk, vrk)
         if np.mod(k, 10) == 0:
             print k
         k += 1

currtime = time.strftime("%Y%m%d_%H%M%S")
fname = "datalog_" + currtime + ".csv"
d03.save_csv(fname)

_data = d03.get_data()

fig, axes = plt.subplots(1,1)

_t = _data[:,0]
_t -= _t[0]
plt.plot(_t, _data[:, 1])
plt.plot(_t, _data[:, 2])
plt.plot(_t, _data[:, 3])
plt.plot(_t, _data[:, 4])
plt.plot(_t, _data[:, 5])

#axes[0,1].plot(_t, _data[:,6])
#axes[1,1].plot(_t, _data[:,7])

