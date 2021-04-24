# run newcomer2_3.py
# inner_atom chain A

from pymol import cmd
import math

def inner_atom(selection='(all)', quiet=1):
    try:
        from itertools import izip
    except ImportError:
        izip = zip
    quiet = int(quiet)
    model = cmd.get_model(selection).atom
    center = cmd.centerofmass(selection)
    x = [i.coord for i in model]
    mass = [i.get_mass() for i in model]
    xm = [(m*i,m*j,m*k) for (i,j,k),m in izip(x,mass)]
    tmass = sum(mass)
    rr = sum(mi*i+mj*j+mk*k for (i,j,k),(mi,mj,mk) in izip(x,xm))
    mm = sum((sum(i)/tmass)**2 for i in izip(*xm))
    rg = math.sqrt(rr/tmass - mm)

    square_dis = [math.sqrt((center[0]-a)**2 + (center[1]-b)**2 + (center[2]-c)**2) for a,b,c in x]
    in_out_radius = [model[idx]  for idx, dis in enumerate(square_dis) if dis - rg < 0]
    for atom in in_out_radius:
        selection = 'rank ' + str(atom.id)
        cmd.color('red', selection, quiet=1)


cmd.extend("inner_atom", inner_atom)