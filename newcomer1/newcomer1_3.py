# $ python3 newcomer1_3.py NT_113952.fasta

import sys
from Bio import SeqIO
from Bio.SeqUtils import *
from Bio.Seq import reverse_complement
import numpy as np
import matplotlib.pyplot as plt

for record in SeqIO.parse(sys.argv[1], 'fasta'):
    ID = record.id
    description = record.description
    sequence = record.seq
    reversed_complimentary_seq = reverse_complement(record.seq)
    width = int(input('please input width :'))
    step = int(input('please input step : '))
    totalGC = np.zeros(len(sequence))
    if sequence[0] == 'G' or sequence[0] == 'C':
        totalGC[0] = 1
    for i in range(1, len(sequence)):
        if sequence[i] == 'G' or sequence[i] == 'C':
            totalGC[i] = totalGC[i-1] + 1
        else:
            totalGC[i] = totalGC[i-1]
    j = 0
    pos = []
    GCcontent = []
    while j + width <= len(sequence):
    	pos.append(j)
    	GCcontent.append((totalGC[width+j] - totalGC[j])/width)
    	j += step
    plt.figure(figsize=(15,4))
    plt.plot(pos, GCcontent)
    plt.title('GC-content change (newcommer 1-3)')
    plt.xlabel("Position")
    plt.ylabel("GCcontent")
    plt.savefig('newcommer1_3.png')