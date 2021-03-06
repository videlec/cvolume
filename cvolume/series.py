from sage.all import *
import time
from admcycles import *
from .utils import *


def monom(par):
    exp = par.to_exp()
    return prod(ZZ(1)/factorial(k) for k in exp)*prod([gens(R)[i-1] for i in par])

def coeff(par):
    if par == Partition([1,1,1]):
        return 1
    elif ((sum([i-1 for i in par])-len(par)+3)/ZZ(3)) in ZZ and ((sum([i-1 for i in par])-len(par)+3)/ZZ(3))>=0:
        n = len(par)
        g = ((sum([i-1 for i in par])-len(par)+3)/ZZ(3)).ceil()
        psi = prod(psiclass(i+1,g,n)**(par[i]-1) for i in range(0,len(par)))
        return psi.evaluate()
    else:
        return 0

t0,t1,t2,t3,t4,t5,t6 = R.gens()[:7]

def get_Fs2(F):
    return 12*diff(F,t2) - diff(F,t0,2)/2 - diff(F,t0)**2/2

def get_Fs3(F):
    return 120*diff(F,t3) - 6*diff(F,t0,t1) - 6*diff(F,t1)*diff(F,t0) + 5*diff(F,t0)/4

def get_Fs4(F):
    return 1680*diff(F, t4) - 18*diff(F, t1, t1) - 18*diff(F, t1)**2 - 60*diff(F, t0, t2) - 60*diff(F, t2)*diff(F, t0) + 7*diff(F, t0, t0, t0)/6 + 7*diff(F, t0)*diff(F, t0, t0)/2 + 7*diff(F, t0)**3/6 + 49*diff(F, t1)/2 - ZZ(35)/96

def get_Fs22(F):
    return ZZ(1)/2*(144*diff(F,t2,t2) - 840*diff(F,t3) - 12*diff(F,t0,t0,t2) - 24*diff(F,t0)*diff(F,t0,t2) + 24*diff(F,t0,t1) + 24*diff(F,t1)*diff(F,t0) + diff(F,t0,4)/4 + diff(F,t0)*diff(F,t0,3) + diff(F,t0,t0)**2/2 + diff(F,t0)**2*diff(F,t0,t0) - 3*diff(F,t0))

def get_Fs5(F):
    return 30240*diff(F, t5) - 360*diff(F, t1, t2) - 360*diff(F, t2)*diff(F, t1) - 840*diff(F, t0, t3) - 840*diff(F, t0)*diff(F, t3) + 27*diff(F, t0, t0, t1) + 27*diff(F, t1)*diff(F, t0, t0) + 54*diff(F, t0)*diff(F, t0, t1) + 27*diff(F, t1)*diff(F, t0)*diff(F, t0) + 585*diff(F, t2) - 105*diff(F, t0, t0)/8 - 105*diff(F, t0)*diff(F, t0)/8

def get_Fs23(F):
    return 1440*diff(F, t2, t3) - 15120*diff(F, t4) - 60*diff(F, t0, t0, t3) - 120*diff(F, t0)*diff(F, t0, t3) - 72*diff(F, t0, t1, t2) - 72*diff(F, t1)*diff(F, t0, t2) - 72*diff(F, t1, t2)*diff(F, t0) + 90*diff(F, t1, t1) + 90*diff(F, t1)**2 + 375*diff(F, t0, t2) + 360*diff(F, t2)*diff(F, t0) + 3*diff(F, t0, t0, t0, t1) + 6*diff(F, t0, t1)*diff(F, t0, t0) + 9*diff(F, t0)*diff(F, t0, t0, t1) + 3*diff(F, t1)*diff(F, t0, t0, t0) + 6*diff(F, t1)*diff(F, t0)*diff(F, t0, t0) + 6*diff(F, t0)**2*diff(F, t0, t1) - 45*diff(F, t0, t0, t0)/8 - 65*diff(F, t0)*diff(F, t0, t0)/4 - 5*diff(F, t0)**3 - 165*diff(F, t1)/2 + ZZ(29)/32

def get_Fs6(F):
    return 665280*diff(F, t6) - 1800*diff(F, t2, t2) - 1800*diff(F, t2)**2 - 5040*diff(F, t1, t3) - 5040*diff(F, t3)*diff(F, t1) - 15120*diff(F, t0, t4) - 15120*diff(F, t4)*diff(F, t0) + 16170*diff(F, t3) + 198*diff(F, t0, t1, t1) + 396*diff(F, t1)*diff(F, t0, t1) + 198*diff(F, t1, t1)*diff(F, t0) + 198*diff(F, t1)**2*diff(F, t0) + 330*diff(F, t0, t0, t2) + 330*diff(F, t2)*diff(F, t0, t0) + 660*diff(F, t0)*diff(F, t0, t2) + 330*diff(F, t2)*diff(F, t0)**2 - 33*diff(F, t0, t0, t0, t0)/8 - 33*diff(F, t0)*diff(F, t0, t0, t0)/2 - 99*diff(F, t0, t0)**2/8 - 99*diff(F, t0)**2*diff(F, t0, t0)/4 - 33*diff(F, t0)**4/8 - 891*diff(F, t0, t1)/2 - 891*diff(F, t1)*diff(F, t0)/2 + 1155*diff(F, t0)/32

def get_Fs24(F):
    return 385*diff(F, t0)*diff(F, t0)/8 + 385*diff(F, t0, t0)/8 - 21*diff(F, t0)*diff(F, t0)*diff(F, t0, t0, t0)/4 - 7*diff(F, t0)*diff(F, t0, t0)*diff(F, t0, t0) - 7*diff(F, t0, t0, t0, t0, t0)/12 - 147*diff(F, t0)*diff(F, t0)*diff(F, t1) - 637*diff(F, t0, t0, t1)/4 + 102*diff(F, t0)*diff(F, t0)*diff(F, t0, t2) + 18*diff(F, t0, t1)*diff(F, t0, t1) - 7*diff(F, t0)*diff(F, t0)*diff(F, t0)*diff(F, t0, t0)/2 + 60*diff(F, t2)*diff(F, t0)*diff(F, t0, t0) - 35*diff(F, t0)*diff(F, t0, t0, t0, t0)/12 - 21*diff(F, t0, t0)*diff(F, t0, t0, t0)/4 - 637*diff(F, t0)*diff(F, t0, t1)/2 + 36*diff(F, t1)*diff(F, t0)*diff(F, t0, t1) + 132*diff(F, t0)*diff(F, t0, t0, t2) + 30*diff(F, t2)*diff(F, t0, t0, t0) + 102*diff(F, t0, t2)*diff(F, t0, t0) + 18*diff(F, t0)*diff(F, t0, t1, t1) + 18*diff(F, t1)*diff(F, t0, t0, t1) - 720*diff(F, t0, t2)*diff(F, t2) - 1680*diff(F, t0)*diff(F, t0, t4) - 720*diff(F, t2, t2)*diff(F, t0) - 432*diff(F, t1, t2)*diff(F, t1) - 720*diff(F, t0, t2, t2) - 840*diff(F, t0, t0, t4) + 44*diff(F, t2, t0, t0, t0) + 20160*diff(F, t2, t4) - 216*diff(F, t1, t1, t2) - 147*diff(F, t1)*diff(F, t0, t0) + 9*diff(F, t1, t1, t0, t0) + 2520*diff(F, t2)*diff(F, t1) + 6720*diff(F, t0)*diff(F, t3) + 6720*diff(F, t0, t3) - 2835*diff(F, t2) + 2814*diff(F, t1, t2) - 332640*diff(F, t5)

def get_Fs33(F):
    return ZZ(1)/2*(14400*diff(F, t3, t3) - 332640*diff(F, t5) - 1440*diff(F, t0, t1, t3) - 1440*diff(F, t1, t3)*diff(F, t0) - 1440*diff(F, t0, t3)*diff(F, t1) + 7020*diff(F, t0, t3) + 6720*diff(F, t0)*diff(F, t3) + 2160*diff(F, t1, t2) + 2160*diff(F, t2)*diff(F, t1) + 36*diff(F, t1, t1, t0, t0) + 36*diff(F, t1, t0)*diff(F, t1, t0) + 36*diff(F, t1, t1)*diff(F, t0, t0) + 72*diff(F, t1)*diff(F, t0, t0, t1) + 72*diff(F, t0)*diff(F, t0, t1, t1) + 36*diff(F, t1)*diff(F, t1)*diff(F, t0, t0) + 72*diff(F, t1)*diff(F, t0)*diff(F, t0, t1) + 36*diff(F, t1, t1)*diff(F, t0)*diff(F, t0) - 2400*diff(F, t2) - 165*diff(F, t0, t0, t1) - 165*diff(F, t1)*diff(F, t0, t0) - 150*diff(F, t1)*diff(F, t0)*diff(F, t0) - 315*diff(F, t0)*diff(F, t0, t1) + 725*diff(F, t0, t0)/16 + 175*diff(F, t0)*diff(F, t0)/4)

def get_Fs7(F):
    return 17297280*diff(F,t7) - 50400*diff(F,t2,t3) - 50400*diff(F,t3)*diff(F,t2) - 90720*diff(F,t1,t4) - 90720*diff(F,t4)*diff(F,t1) - 332640*diff(F,t0,t5) - 332640*diff(F,t5)*diff(F,t0) + 468*diff(F,t1,t1,t1) + 1404*diff(F,t1)*diff(F,t1,t1) + 468*diff(F,t1)**3 + 4680*diff(F,t0,t1,t2) + 4680*diff(F,t1)*diff(F,t0,t2) + 4680*diff(F,t2)*diff(F,t0,t1) + 4680*diff(F,t1,t2)*diff(F,t0) + 4680*diff(F,t2)*diff(F,t1)*diff(F,t0) + 5460*diff(F,t0,t0,t3) + 5460*diff(F,t3)*diff(F,t0,t0) + 10920*diff(F,t0)*diff(F,t0,t3) + 5460*diff(F,t3)*diff(F,t0)**2 + 507780*diff(F,t4) - 10725*diff(F,t0,t2) - 10725*diff(F,t2)*diff(F,t0) - 5577*diff(F,t1,t1)/2 - 5577*diff(F,t1)**2/2 - 143*diff(F,t0,t0,t0,t1) - 143*diff(F,t1)*diff(F,t0,t0,t0) - 429*diff(F,t0,t1)*diff(F,t0,t0) - 429*diff(F,t0)*diff(F,t0,t0,t1) - 429*diff(F,t0)**2*diff(F,t0,t1) - 429*diff(F,t1)*diff(F,t0)*diff(F,t0,t0) - 143*diff(F,t1)*diff(F,t0)**3 + 1001*diff(F,t0,t0,t0)/8 + 3003*diff(F,t0)*diff(F,t0,t0)/8 + 1001*diff(F,t0)**3/8 + 27027*diff(F,t1)/16 - ZZ(5005)/384

def get_Fs222(F):
    return ZZ(1)/6*(1728*diff(F,t2,t2,t2) - 30240*diff(F,t2,t3) - 216*diff(F,t0,t0,t2,t2) - 432*diff(F,t0,t2)**2 - 432*diff(F,t0)*diff(F,t0,t2,t2) + 864*diff(F,t0,t1,t2) + 864*diff(F,t1)*diff(F,t0,t2) + 864*diff(F,t1,t2)*diff(F,t0) + 1260*diff(F,t0,t0,t3) + 2520*diff(F,t0)*diff(F,t0,t3) + 9*diff(F,t0,t0,t0,t0,t2) + 36*diff(F,t0,t2)*diff(F,t0,t0,t0) + 36*diff(F,t0)*diff(F,t0,t0,t0,t2) + 36*diff(F,t0,t0)*diff(F,t0,t0,t2) + 72*diff(F,t0)*diff(F,t0,t2)*diff(F,t0,t0) + 36*diff(F,t0)**2*diff(F,t0,t0,t2) + 151200*diff(F,t4) - 576*diff(F,t1,t1) - 576*diff(F,t1)**2 - 2628*diff(F,t0,t2) - 2520*diff(F,t2)*diff(F,t0) - 36*diff(F,t0,t0,t0,t1) - 108*diff(F,t0)*diff(F,t0,t0,t1) - 36*diff(F,t1)*diff(F,t0,t0,t0) - 72*diff(F,t0,t1)*diff(F,t0,t0) - 72*diff(F,t1)*diff(F,t0)*diff(F,t0,t0) - 72*diff(F,t0)**2*diff(F,t0,t1) - (ZZ(1)/8)*diff(F,t0,t0,t0,t0,t0,t0) - (ZZ(3)/4)*diff(F,t0)*diff(F,t0,t0,t0,t0,t0) - (ZZ(3)/2)*diff(F,t0,t0)*diff(F,t0,t0,t0,t0) - (ZZ(5)/4)*diff(F,t0,t0,t0)**2 - 6*diff(F,t0)*diff(F,t0,t0)*diff(F,t0,t0,t0) - diff(F,t0,t0)**3 - (ZZ(3)/2)*diff(F,t0)**2*diff(F,t0,t0,t0,t0) - 3*diff(F,t0)**2*diff(F,t0,t0)**2 - diff(F,t0)**3*diff(F,t0,t0,t0) + (ZZ(63)/2)*diff(F,t0,t0,t0) + 90*diff(F,t0)*diff(F,t0,t0) + 27*diff(F,t0)**3 + 378*diff(F,t1) - ZZ(63)/20)

class PartitionFunctions:
    AC_formulae = {(2,):get_Fs2, (3,):get_Fs3, (4,):get_Fs4, (2,2):get_Fs22, (5,):get_Fs5, (2,3):get_Fs23, (6,):get_Fs6,\
                   (2,4):get_Fs24, (3,3):get_Fs33, (7,):get_Fs7, (2,2,2):get_Fs222}
    shifts = {(2,):3, (3,):4, (4,):5, (2,2):6, (5,):6, (2,3):7, (6,):7, (2,4):8, (3,3):8, (7,):8, (2,2,2):9}
    times = {():time_for_F, (2,):time_for_Fs2, (3,):time_for_Fs3, (4,):time_for_Fs4, (2,2):time_for_Fs22, (5,):time_for_Fs5,\
             (2,3):time_for_Fs23, (6,):time_for_Fs6,(2,4):time_for_Fs24, (3,3):time_for_Fs33, (7,):time_for_Fs7,\
             (2,2,2):time_for_Fs222}
    def __init__(self):
        self.max_weights = {}
        self.polynomials = {}
        self.verbose = False
    
    def partition_function(self,w):
        F_max_weight = self.max_weights.get((),-1)
        F = self.polynomials.get((),R.zero()) 
        if w > F_max_weight:
            tic = time.time()
            time_est = time_for_F(w) - time_for_F(F_max_weight)
            if time_est > 120:
                command = input(f"    Partition function update might take more than {float2time(time_est,2)}. Do you want to \
                continue? Print 'n' to abort, to continue press Enter.")
                if command == 'n':
                    sys.exit("The computation was aborted by user due to time constraints.")
            if self.verbose: print(f"    Updating the partition function F from max_weight {F_max_weight} to {w}...Estimated time: {float2time(time_est,2)}")
            for i in range(max(F_max_weight,0)+1,w+1):
                F += sum(coeff(par)*monom(par) for par in Partitions(i))
            self.max_weights[()] = w
            self.polynomials[()] = F
            toc = time.time()
            if self.verbose: print(f"    Done updating the partition function F from max_weight {F_max_weight} to {w} in: {float2time(toc-tic,2)}")
        return F
    
    def __call__(self, s_part, w):
        Fs_max_weight = self.max_weights.get(s_part,-1)
        Fs = self.polynomials.get(s_part,R.zero())             
        if w > Fs_max_weight:
            tic = time.time()
            time_est = self.times[s_part](w)
            if time_est > 120:
                command = input(f"Fs function update for s = {s_part}, w = {w} might take more than {float2time(time_est,2)}.\
                Do you want to continue? Print 'n' to abort, to continue press Enter..")              
                if command == 'n':
                    sys.exit("The computation was aborted by user due to time constraints.")
            if self.verbose: print(f"Updating Fs function for s = {s_part} from max_weight {Fs_max_weight} to {w}...Estimated time: {float2time(time_est,2)}")
            F = self.partition_function(w+self.shifts[s_part])
            Fs = self.AC_formulae[s_part](F)
            self.max_weights[s_part] = w
            self.polynomials[s_part] = Fs
            toc = time.time()
            if self.verbose: print(f"Done updating Fs function for s = {s_part} from max_weight {Fs_max_weight} to {w} in: {float2time(toc-tic,2)}")     
        return Fs
                              

Fs = PartitionFunctions()