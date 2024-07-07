#!/usr/bin/python

import numpy
import sys 
import os
try :
    x = int(sys.argv[1])
# Error control, no need to touch
except IndexError :
    raise IndexError("It seems you are calling this script with too few arguments.")
except ValueError :
    raise ValueError("It seems some of the arguments are not correctly formatted. "+
                     "Remember that they must be integers.")

log10_a_table = [-0.73, -0.1, -5]
log10_kstar_table = [8.14, 9.25, 3]
delta_table = [1.46, 2.45, 1.3]

def pps(k, a, kstar, delta):
    a_s =  2.0989e-9
    n_s = 0.9649
    k_pivot = 0.05
    return (a_s*(k/k_pivot)**(n_s-1) + a/(numpy.sqrt(2*numpy.pi)*delta)*numpy.exp(-(numpy.log(k/kstar))**2/(2*delta*delta)))

def casex_pps(k, x):
    return pps(k, 10**(log10_a_table[x]), 10**(log10_kstar_table[x]), delta_table[x])

# 3. Limits for k and precision:
#    Check that the boundaries are correct for your case.
#    It is safer to set k_per_decade primordial slightly bigger than that of Class.

k_min  = 1.e-7
k_max  = 10.e10
k_per_decade_primordial = 200.

#
# And nothing should need to be edited from here on.
#

# Filling the array of k's
ks = [float(k_min)]
while ks[-1] < float(k_max) :
    to_append = ks[-1]*10.**(1./float(k_per_decade_primordial))
    if to_append < k_max:
        ks.append(to_append)
    else:
        break

# Filling the array of Pk's
for k in ks :
    P_k = casex_pps(k, x)
    print("%.18g %.18g" % (k, P_k))
