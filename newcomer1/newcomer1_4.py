# $ python3 newcomer1_4.py NT_113952.fasta 

import sys
from Bio import SeqIO
from Bio.SeqUtils import *
from Bio.Seq import reverse_complement, Seq

part_seq = Seq(sys.argv[2])

for record in SeqIO.parse(sys.argv[1], 'fasta'):
    i = 0
    j = 0
    ID = record.id
    description = record.description
    sequence = record.seq
    reversed_complimentary_seq = reverse_complement(record.seq)
    print('Search [' + part_seq + '] in sequence')
    try:
        while True:
            search_seq = sequence[i:]
            pos = search_seq.index(part_seq) + i+1
            print(str(pos) + '-' + str(pos + len(part_seq)))
            i = pos
    except ValueError:
        pass
    print('Search [' + part_seq + '] in reversed complimentary sequence')
    try:
        while True:
            search_seq = reversed_complimentary_seq[j:]
            pos = search_seq.index(part_seq) + j+1
            print(str(pos) + '-' + str(pos + len(part_seq)))
            j = pos
    except ValueError:
        pass
    