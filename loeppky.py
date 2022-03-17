#!/usr/bin/python3

import numpy as np
    
fp = open('input.csv', 'r')
x = np.array(fp.readline().split(',')).astype('float')
fp.close()

x1 = x[0]
x2 = x[1]
x3 = x[2]
x4 = x[3]
x5 = x[4]
x6 = x[5]
x7 = x[6]

term1 = 6*x1 + 4*x2
term2 = 5.5*x3 + 3*x1*x2
term3 = 2.2*x1*x3 + 1.4*x2*x3
term4 = x4 + 0.5*x5
term5 = 0.2*x6 + 0.1*x7

ans = term1 + term2 + term3 + term4 + term5

# output csv file
header = 'f'
np.savetxt('output.csv', ans.reshape([-1,1]),
           delimiter=",", comments='',
           header=header)
