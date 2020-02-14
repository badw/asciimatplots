import warnings
from pymatgen.io.vasp import Vasprun as pymvasprun
import numpy as np 
import termplotlib as tp
from colorama import Fore
warnings.filterwarnings("ignore")

def main():
    vasprun = pymvasprun('./vasprun.xml')
    tot = []
    for i in range(0,len(vasprun.as_dict()['output']['ionic_steps'])):
        x = [x2[0] for x2 in vasprun.as_dict()['output']['ionic_steps'][i]['forces']]
        y = [y2[1] for y2 in vasprun.as_dict()['output']['ionic_steps'][i]['forces']]
        z = [z2[2] for z2 in vasprun.as_dict()['output']['ionic_steps'][i]['forces']]
        total = np.amax([np.sqrt(x[i]**2 + y[i]**2 + z[i]**2) for i in range(0,len(x))])
        tot.append(total)
    energies = [ e['e_wo_entrp'] for e in vasprun.as_dict()['output']['ionic_steps']]
    x = [x for x in range(1,len(tot)+1)]
    
    '''
    plotting maximum force
    '''
    fig1 = tp.figure()
    fig1.plot(x,tot,width=60,height=20,label='Fmax',xlabel='ionic step')
    
    figure1 = []
    for string in fig1.get_string():
        if string == '*':
            figure1.append(Fore.RED + string)
        else:
            figure1.append(Fore.WHITE + string)
    
    print(''.join(figure1))
    
    '''
    plotting total energy
    '''
    fig2 = tp.figure()
    fig2.plot(x,energies,width=60,height=20,label='Etot',xlabel='ionic step')
    
    figure2 = []
    for string in fig2.get_string():
        if string == '*':
            figure2.append(Fore.GREEN + string)
        else:
            figure2.append(Fore.WHITE + string)
    
    print(''.join(figure2))

if __name__ == "__main__":
    main()
