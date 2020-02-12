#!/usr/bin/env python3

import pickle
import os

data = 'files.dat'
HOME = os.getenv('HOME')
DX2DIR = (HOME + '/.DX2')
AKADIR = (DX2DIR + '/aliases')
FUNCDIR = (DX2DIR + '/functions')
fileCDFUNC = (FUNCDIR + '/cd.func')
fileMDFUNC = (FUNCDIR + '/md.func')
fileLSAKA = (AKADIR + '/ls.aka')
fileMISCAKA = (AKADIR + '/misc.aka')
fileDX2RC = (HOME + '/.dx2rc')

f = open(data, 'rb')

files = pickle.load(f)
f.close()

def writefile(x, y):
	"""
	Function used to:
		1. check to see if file already exists
			1a. Move on if it already exists
			1b. or, create the file if it doesn't exists
	Syntax:
		writefile(<file's path>, <file's data>)
	"""
	filepath = str(x)
	filedata = y
	print('\033[00;01mChecking for \033[00;38;5;226m' + filepath + '\033[00;01m:\033[m')
	if os.path.exists(filepath) == True:
		print('\t\033[00;01mFile already exists')
	else:
		print('\t\033[00;01mFile not found. Creating now: ', end='')
		f = open(filepath, 'w')
		f.write(filedata)
		f.close()
		print('\033[00;01;38;5;46mDONE\033[m')

def writealldefault():
	"""
	Func to write all the default files:
		1.	.dx2rc
		2.	all the aka files
		3.	all the func files
	"""
	writefile(fileDX2RC, files['.dx2rc'])
	writefile(fileLSAKA, files['ls.aka'])
	writefile(fileMISCAKA, files['misc.aka'])
	writefile(fileCDFUNC, files['cd.func'])
	writefile(fileMDFUNC, files['md.func'])
