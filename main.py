# Homo sapiens chromosome 6, GRCh38.p14 Primary Assembly is used as an example
# NCBI Reference Sequence: NC_000006.12
# https://www.ncbi.nlm.nih.gov/nuccore/NC_000006.12?report=fasta&from=27866792&to=27867588&strand=true

# 1. libraries and data import
import time
import datetime
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
import os

# 2. enter variables
start_time = time.time()
end_time = time.time()
NCBIWWW.email = '' # there should be an email here 

# 3. send a request to BLAST, write the result to an XML file
wdir = os.getcwd()
record = SeqIO.read(handle='sequence.fasta', format='fasta')
request = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))

with open('blast_result.xml', 'w+') as add_to:
    add_to.write(request.read())
    request.close()

# 4. output the result and program execution time
print(f'Time used: {end_time - start_time}.')

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


# 5. copy XML request file to target_url repository

original_file_path = '' # there should be the path to the original file
current_date = datetime.datetime.now() # current time and date

# create a new filename based on the date and time
new_file_name = current_date.strftime('%Y-%m-%d_%H-%M-%S') + '.xml'

# duplicate the file to the new location
new_file_path = os.path.join('C:\\', new_file_name) # there should be the destination directory path
os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
with open(original_file_path, 'rb') as original_file:
    with open(new_file_path, 'wb') as new_file:
        new_file.write(original_file.read())

'''                   ! optional element !
if __name__ == '__main__':
    pass
'''
