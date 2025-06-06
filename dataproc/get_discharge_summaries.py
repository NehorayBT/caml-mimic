"""
    Reads discharge file, finds the discharge summaries, preprocesses them and writes out the filtered dataset.
"""
import csv

from nltk.tokenize import RegexpTokenizer

from tqdm import tqdm

from constants import MIMIC_4_DIR

#retain only alphanumeric
tokenizer = RegexpTokenizer(r'\w+')

#note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text

def write_discharge_summaries(out_file):
    notes_file = '%s/discharge.csv' % (MIMIC_4_DIR)
    print("processing notes file")
    with open(notes_file, 'r', encoding='ISO-8859-1') as csvfile:
        with open(out_file, 'w') as outfile:
            print("writing to %s" % (out_file))
            outfile.write(','.join(['SUBJECT_ID', 'HADM_ID', 'CHARTTIME', 'TEXT']) + '\n')
            notereader = csv.reader(csvfile)
            #header
            next(notereader)
            i = 0
            for line in tqdm(notereader):
                subj = int(line[1])
                category = line[3]
                if category == "DS":
                    note = line[7]
                    #tokenize, lowercase and remove numerics
                    tokens = [t.lower() for t in tokenizer.tokenize(note) if not t.isnumeric()]
                    text = '"' + ' '.join(tokens) + '"'
                    outfile.write(','.join([line[1], line[2], line[5], text]) + '\n')
                i += 1
    return outfile
