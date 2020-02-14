import warnings
from pymatgen.io.vasp import Vasprun
import numpy as np 
import termplotlib as tp
from colorama import Fore
import argparse
import os
from pymatgen.analysis import transition_state


warnings.filterwarnings("ignore")
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fmax', default=False, action='store_true',
                        help='generate a fmax plot only (default=false)')
    parser.add_argument('-e', '--energy', default=False, action='store_true',
                        help='generate an energy barrier plot only (default=false)')
    args = parser.parse_args()

    def nebenergyplot():
        neb = transition_state.NEBAnalysis.from_dir('./')
        
        energies = neb.as_dict()['energies']                                                                                                                 
        norm = [ i - min(energies) for i in energies]  
        image = [x for x in range(0,len(norm))]
        fig1 = tp.figure()
        fig1.plot(image,norm,width=30,height=20,label='Emig',xlabel='image')
        
        figure1 = []
        for string in fig1.get_string():
            if string == '*':
                figure1.append(Fore.GREEN + string)
            else:
                figure1.append(Fore.WHITE + string)
        
        print(''.join(figure1))
    
    def nebforceplot():
        neb = transition_state.NEBAnalysis.from_dir('./')
        
        forces = neb.as_dict()['forces']                                                                                                                 
        image = [x for x in range(0,len(forces))]
        fig2 = tp.figure()
        fig2.plot(image,forces,width=30,height=20,label='Fmax',xlabel='image')
        
        figure2 = []
        for string in fig2.get_string():
            if string == '*':
                figure2.append(Fore.RED + string)
            else:
                figure2.append(Fore.WHITE + string)
        
        print(''.join(figure2))
   
    if args.fmax == True:
        nebforceplot()
    elif args.energy == True:
        nebenergyplot()
    else:
        nebforceplot()
        nebenergyplot()

if __name__ == "__main__":
    main()
