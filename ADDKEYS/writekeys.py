#!/usr/bin/env python3

import os
import sys
import pickle

FILENAME = 'booeysays_rsa_github'
HOME = os.getenv('HOME')
SSHDIR = (HOME + '/.ssh')
PRIKEY = (SSHDIR + '/' + FILENAME)
PUBKEY = (SSHDIR + '/' + FILENAME + '.pub')

#print("Enter filename to use for keys, or hit [Enter] and leave it blank to use\nthe default (" + FILENAME + ") filename.")
print("The default location to create the keys is:\n\t" + SSHDIR + "\n\nEnter another location to use, or hit [Enter] to use the default location.")

print("The default filenames that will be used for the keys are:\n\t1). " + FILENAME + "\n\t2). " + FILENAME + ".pub\n\nEnter another filename to use, or hit [Enter] to use the default filenames.")
newFilename = input(': ')

#f = open('keys.dat', 'rb')
#keys = pickle.load(f)
#f.close()
