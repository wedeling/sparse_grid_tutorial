#!/usr/bin/python3

import numpy as np
    
fp = open('input.csv', 'r')
x = np.array(fp.readline().split(',')).astype('float')
fp.close()

Sw      = x[0]
Wfw     = x[1]
A       = x[2]
LamCaps = x[3] * (np.pi / 180)
q       = x[4]
lam     = x[5]
tc      = x[6]
Nz      = x[7]
Wdg     = x[8]
Wp      = x[9]

fact1 = 0.036 * Sw**0.758 * Wfw**0.0035;
fact2 = (A / ((np.cos(LamCaps))**2))**0.6;
fact3 = q**0.006 * lam**0.04;
fact4 = (100*tc / np.cos(LamCaps))**(-0.3);
fact5 = (Nz*Wdg)**0.49;

term1 = Sw * Wp;

ans = fact1*fact2*fact3*fact4*fact5 + term1;

# output csv file
header = 'f'
np.savetxt('output.csv', ans.reshape([-1,1]),
           delimiter=",", comments='',
           header=header)
