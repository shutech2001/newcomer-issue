# $ python3 newcomer1_3.py NT_113952.fasta

import sys
from Bio import SeqIO
from Bio.SeqUtils import *
from Bio.Seq import reverse_complement
import matplotlib.pyplot as plt

for record in SeqIO.parse(sys.argv[1], 'fasta'):
    ID = record.id
    description = record.description
    sequence = record.seq
    reversed_complimentary_seq = reverse_complement(record.seq)
    width = int(input('please input width :'))
    step = int(input('please input step : '))
    i = 0
    pos = []
    GCcontent = []
    while i + width <= len(sequence):
    	pos.append(i)
    	GCcontent.append(GC(sequence[i:i + width]) / 100)
    	i += step
    plt.figure(figsize=(10,4))
    plt.plot(pos, GCcontent)
    plt.title('GC-content change (newcommer 1-3)')
    plt.xlabel("Position")
    plt.ylabel("GCcontent[%]")
    plt.savefig('newcommer1_3.png')