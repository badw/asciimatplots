import warnings
import numpy as np 
import termplotlib as tp
from colorama import Fore
import argparse
import os
import re
import sys

warnings.filterwarnings("ignore")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', default=False, action='store_true',
                        help='generate a both fmax and energy plots (default=false)')
    parser.add_argument('-e', '--energy', default=False, action='store_true',
                        help='generate a total energy plot only (default=false)')
    parser.add_argument('-s', '--steprange', metavar='step', nargs=2, type=int, default=[1,-1],
                        help='1-indexed min and max steps to show (default:[1,-1])')
    args = parser.parse_args()
    
    if os.path.exists('./OUTCAR'):
        
        def forceplot():
                
            driftlines = []
            sigma = []
            with open("OUTCAR") as outcar:
                for i,line in enumerate(outcar):
                    if 'NIONS' in line:
                        nion = line.split()[-1]
                    if 'total drift' in line:
                        driftlines.append(i)
                    if 'y=' in line:
                        sigma.append(line.split()[-1])

                outcar = open('OUTCAR')
                lines = outcar.readlines()
                
                forces = [" ".join(lines[int(x-(int(nion)+1)):x-1]).split() for x in driftlines]
                 
                newforces = [np.reshape(x, (int(nion), 6)) for x in forces]

                newnewforces = []
                for step in range(len(forces)):
                    newnewforces.append([])
                    for atom in range(int(nion)):        
                        newnewforces[step].append([float(newforces[step][atom][3]),float(newforces[step][atom][4]),float(newforces[step][atom][5])])
                
                fmaxes = []
                for i,x in enumerate(newnewforces):
                    fmaxes.append([])
                    for y in x:
                        fmaxes[i].append(np.linalg.norm(y))
                
                fmax = [np.amax(x) for x in fmaxes]

                numsteps = len(fmax)
                x = [x for x in range(1,numsteps+1)]
                minstep = 0 if args.steprange[0] <= 1 else args.steprange[0]-1
                maxstep = -1 if args.steprange[1] >= x[-1] or args.steprange[1] == -1 else args.steprange[1]-1
            
            fig1 = tp.figure()
            fig1.plot(x[minstep:maxstep],fmax[minstep:maxstep],
                    width=40,
                    height=20,
                    label='Fmax',
                    xlabel='ionic step')
            
            figure1 = []
            for string in fig1.get_string():
                if string == '*':
                    figure1.append(Fore.RED + string)
                else:
                    figure1.append(Fore.WHITE + string)
            
            print(''.join(figure1))
        
        def energyplot():
            sigma = []
            with open("OUTCAR") as outcar:
                for line in outcar:
                    if 'y=' in line:
                        sigma.append(float(line.split()[-1]))
            

            numsteps = len(sigma)
            x = [x for x in range(1,numsteps+1)]
            minstep = 0 if args.steprange[0] <= 1 else args.steprange[0]-1
            maxstep = -1 if args.steprange[1] > x[-1] or args.steprange[1] == -1 else args.steprange[1]-1

            fig2 = tp.figure()
            fig2.plot(x[minstep:maxstep],sigma[minstep:maxstep],
                    width=40,
                    height=20,
                    label='Etot',
                    xlabel='ionic step')
            
            figure2 = []
            for string in fig2.get_string():
                if string == '*':
                    figure2.append(Fore.GREEN + string)
                else:
                    figure2.append(Fore.WHITE + string)
            
            print(''.join(figure2))
   
        if args.all == True:
            forceplot()
            energyplot()
        elif args.energy == True:
            energyplot()
        else:
            forceplot()
    else:
        print('OUTCAR not found')


if __name__ == "__main__":
    main()
