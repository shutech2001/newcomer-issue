# $ python3 newcomer1_5.py NT_113952.fasta 

import sys
from Bio import SeqIO
from Bio.SeqUtils import *
from Bio.Seq import reverse_complement, Seq

file_path = 'newcommer1_5/translate.txt'

for record in SeqIO.parse(sys.argv[1], 'fasta'):
    ID = record.id
    description = record.description
    sequence = record.seq
    reversed_complimentary_seq = reverse_complement(record.seq)

    f = open(file_path, 'w')

    for i in range(3):
        f.write('Reading frame ' + str(i+1) + ' (sequence)\n')
        translate_seq = sequence[i:].translate()
        try:
            while True:
                start_seq = translate_seq.index('M')
                end_seq = start_seq + translate_seq[start_seq:].index('*')
                f.write(str(translate_seq[start_seq : end_seq + 1]) + '\n')
                translate_seq = translate_seq[end_seq + 1:]
        except ValueError:
            pass
    for i in range(3):
        f.write('Reading frame ' + str(i+1) + ' (reversed complimentary sequence)\n')
        translate_rev_cseq = reversed_complimentary_seq[i:].translate()
        try:
            while True:
                start_seq = translate_rev_cseq.index('M')
                end_seq = start_seq + translate_rev_cseq[start_seq:].index('*')
                f.write(str(translate_rev_cseq[start_seq : end_seq + 1]) + '\n')
                translate_rev_cseq = translate_rev_cseq[end_seq + 1:]
        except ValueError:
            pass
    f.close()