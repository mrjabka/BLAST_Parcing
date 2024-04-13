# 1. libraries and data import, reference data
import time
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
import os

# 2. enter variables
start_time = time.time()
end_time = time.time()
NCBIWWW.email = 'anikeeew@gmail.com'

# 3. send a request to BLAST, write the result to an XML file
wdir = os.getcwd()
record = SeqIO.read(handle='sequence.fasta', format='fasta')
request = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))

with open('blast_result.xml', 'w+') as add_to:
    add_to.write(request.read())
    request.close()

# 4. output the result and program execution time
print(f'Time used: {end_time-start_time}.')

result_handle = open('blast_result.xml', 'r')
blast_record = NCBIXML.read(result_handle)
E_VALUE_THRESH = 0.001
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            print('Sequence:', alignment.title)
            print('Sequence length:', alignment.length)
            print('E-value:', hsp.expect)
            print(hsp.query[0:75] + '...')
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')