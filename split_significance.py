#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  21 11:48:18 2018

@author: denise

File for splitting the clinical significance in multiple patients line
"""

from optparse import OptionParser

# Get the input and output file paths 
parser = OptionParser()
parser.add_option("-i", "--input", dest="input", help="The input file name")
parser.add_option("-o", "--output", dest="output", help="The output file name")

(options, args) = parser.parse_args()
data_file = options.input
end_file = options.output

# Open both files
open_file = open(data_file, "r")
open_end_file = open(end_file, "w")
# The file should be a tab-separated MAF file
for line in open_file:
    # MAF files has the CLIN_SIG column at position 86
    significance_column = line.split("\t")[85]
    if ',' in significance_column:
        # The significances are separated by comma's
        all_sig = significance_column.split(',')
        for sig in all_sig:
            new_line = line.replace(significance_column, sig)
            open_end_file.write(new_line)
    # Change nothing if there is just one clinical significance defined
    else:
        # add the line to the new file
        open_end_file.write(line)
        
open_file.close()
open_end_file.close()