# $ python3 newcomer1_2.py NT_113952.fasta

import sys
from Bio import SeqIO
from Bio.Seq import reverse_complement

for record in SeqIO.parse(sys.argv[1], 'fasta'):
    id = record.id
    description = record.description
    sequence = record.seq
    reversed_complimentary_seq = reverse_complement(record.seq)
    print("ID          : " + id)
    print("description : " + description)
    print("revcomp seq : " + reversed_complimentary_seq)