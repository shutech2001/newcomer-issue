# $ python3 newcomer1_1.py NT_113952.fasta

import sys
from Bio import SeqIO

for record in SeqIO.parse(sys.argv[1], 'fasta'):
    ID = record.id
    description = record.description
    sequence = record.seq
    num_A = sequence.count('A')
    num_T = sequence.count('T')
    num_G = sequence.count('G')
    num_C = sequence.count('C')
    print("ID          : " + ID)
    print("description : " + description)
    print("A           : " + str(num_A))
    print("T           : " + str(num_T))
    print("G           : " + str(num_G))
    print("C           : " + str(num_C))