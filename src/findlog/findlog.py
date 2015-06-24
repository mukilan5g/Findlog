#!/usr/bin/env python
import re 
import argparse
from sys import argv
from collections import Counter, defaultdict
from os import listdir
from os.path import isfile, join


def get_files_in_dir(path):
    return [ file for file in listdir(path) 
            if isfile(
            join(path,file)) ]

def search_files_by_re(file):
    path = file.split('\\')
    files_in_directory = get_files_in_dir('\\'.join(path[:len(path)-1]))
    return [ '\\'.join(path[:len(path)-1])+'\\'+file for file in files_in_directory
	        if re.match(path[len(path)-1], file)]
		    
def list_all_match(patterns):
    list_of_files=defaultdict(list)
    for pattern in patterns:
        for file_pattern in (open('E:\\git\\skeleton\\src\\findlog\\.files', 'r').read()).split('\n'):
            for file in search_files_by_re(file_pattern):
                if re.search(pattern, open(file, 'r').read()):
                    list_of_files[pattern].append(file)
    return list_of_files

def list_anything_match(patterns):
    files  = iter(list_all_match(patterns).values())
    match_file = files.next()
    while True:
        try:
            match_file = set(match_file) & set(files.next())
        except StopIteration:
            return 	{str(patterns): list(match_file)}	

def display(match):
    if match == {}:
	    print '[No file mathches with the words]'
    else:
        for pattern, files in match.iteritems():
            print '--'+str(pattern)+'--\n'
            for file in files:
                print str(file)+'\n'

def findall(patterns, type):
    if type == 'or':
       display(list_all_match(patterns))
    else:
       display(list_anything_match(patterns))
    raw_input()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('patterns', nargs='*')
    parser.add_argument('-o', action='store_true', dest='type')
    args = parser.parse_args()
    if args.type:
        findall(args.patterns, 'or')
    else:
        findall(args.patterns, 'and')	
        
    