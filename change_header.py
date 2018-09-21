#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:37:54 2018

@author: denise

Script for change a column name of the header
"""

from optparse import OptionParser

class ReplaceColumnName(object):
    
    def get_arguments(self):
        parser = OptionParser()
        parser.add_option("-i", "--input", dest="input", 
                          help="The input file name")
        parser.add_option("-p", "--previous", dest="previous", 
                          help="Column name to replace")
        parser.add_option("-n", "--new", dest="new", 
                          help="New name for the column")
        parser.add_option("-o", "--output", dest="output", 
                          help="The output file name")
        
        (options, args) = parser.parse_args()
        self.input_file = options.input
        self.old_name = options.previous
        self.new_name = options.new
        self.output_file = options.output

    def parse_header(self):
        open_input_file = open(self.input_file, "r")
        open_output_file = open(self.output_file, "w")
        for index, line in enumerate(open_input_file):
            if index == 0:
                header = line
                new_header = header.replace(self.old_name, self.new_name)
                open_output_file.write(new_header)
            else:
                open_output_file.write(line)
        open_input_file.close()
        open_output_file.close()

if __name__ == "__main__":
    rc = ReplaceColumnName()
    rc.get_arguments()
    rc.parse_header()