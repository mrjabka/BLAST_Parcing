# 1. libraries and data import
import time
import datetime
import shutil
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
import os

# 2. enter variables
start_time = time.time()
end_time = time.time()
NCBIWWW.email = '' # there should be an email here without file name
url = '' # there should be a path to the file
target_url = '' # there should be a destination directory
file_name = 'blast_result.xml'

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

# set the path to the original file
original_file_path = 'C:\\Users\\anike\\OneDrive\\Документы\\py_project\\blast_result.xml'

# get the current date and time
current_date = datetime.datetime.now()

# create a new filename based on the date and time
new_file_name = current_date.strftime('%Y-%m-%d_%H-%M-%S') + '.xml'

# duplicate the file to the new location
new_file_path = os.path.join('C:\\Users\\anike\\OneDrive\\Документы\\py_project\\blast_requests', new_file_name)
os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
with open(original_file_path, 'rb') as original_file:
    with open(new_file_path, 'wb') as new_file:
        new_file.write(original_file.read())
