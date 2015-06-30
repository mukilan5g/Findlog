#!/usr/bin/env python
import re, os
import argparse
from sys import argv
from collections import Counter, defaultdict
from os import listdir
from os.path import isfile, join


def get_files_in_dir(path):
    ''' This function takes the path and return only the list files in that leaf directory.
	    
		for example:
		get_files_in_dir(C:\users\mukilan\desktop)
		
		output:
		['new_file.txt','setup.py']
		'''
    return [ file for file in listdir(path) 
            if isfile(
            join(path,file)) ]

def search_files_by_re(file):
    ''' This function takes the full path of the file. If the file name is a regular expression,
	    it checks for the match of the pattern and returns the file.
		
		for example:
		search_files_by_re('C:\\users\\radhu\\desktop\\[a-z0-9]*.py$')
		
		output:
		['C:\\users\\radhu\\desktop\\webcrawl1.py']
		
		note:
		Always specify the path with '\\',don't use '\'.Because the function won't read.It will 
		throw this error:
		{WindowsError: [Error 123] The filename, directory name, or volume label syntax is incorrect:}
	'''
    path = file.split('\\')
    files_in_directory = get_files_in_dir('\\'.join(path[:len(path)-1]))
    return [ '\\'.join(path[:len(path)-1]) + '\\' + file for file in files_in_directory
	        if re.match(path[len(path)-1], file) ]
		    
def get_files_match_any(patterns):
    '''This function takes the list of patterns and return the files which contains the contents
	   matches those patterns anywhere in the file.
	   It will return all files if any one of the pattern matches with the file contents.
	   
	   for example:
	   get_files_match_any(['^w', '^i'])
	   
	   output:
	   defaultdict(<type 'list'>, {'^w': ['C:\\Users\\Radhu\\Desktop\\webcrawl1.py']})
	'''
    list_of_files ={}
    for pattern in patterns:
        list_of_files[pattern] = []
    for pattern in patterns:
        for file_pattern in (open(r'C:\Users\Radhu\Desktop\findlog\src\testfiles\.files', 'r').read()).split('\n'):
            for file in search_files_by_re(os.path.abspath(file_pattern)):
                if re.search(pattern, open(file, 'r').read()):
                    list_of_files[pattern].append(file)
    return list_of_files

def get_files_match_all(patterns):
    '''This function takes the list of patterns and return the files which contains the contents 
	matches those patterns anywhere in the file.
	It will return all files only if all the pattern matches with the file contents.
	
	for example:
	get_files_match_all(['^[a-z]','[a-z]$'])
	
	output:
	{"['^[a-z]', '[a-z]$']": ['C:\\Users\\Radhu\\Desktop\\webcrawl1.py']}
	'''
    files  = iter(get_files_match_any(patterns).values())
    match_file = set(files.next())
    while True:
        try:
            match_file = set(match_file) & set(files.next())
        except StopIteration:
            return 	{str(patterns): list(match_file)}	

def display(match):
    for pattern, files in match.iteritems():
        print '--'+str(pattern)+'--\n'
        if files == []:
            print '[No file match with this pattern]'
        else:
            for file in files:
                print str(file)+'\n'

def findall(patterns, type):
    if type == 'or':
       display(get_files_match_any(patterns))
    else:
       display(get_files_match_all(patterns))
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
        
    