import PyPDF2
import os
import sys

input_folder = sys.argv[1]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        # print(pdf)
        merger.append(pdf)
    
    merger.write('super.pdf')


pdf_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.pdf')]

pdf_combiner(pdf_files)