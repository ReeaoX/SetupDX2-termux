#!/usr/bin/env python3

import pickle

datafile = 'sshkeysetup.dat'

sshkeyPub = 'booeysays_rsa_github.pub'
sshkeyPri = 'booeysays_rsa_github'

f = open(datafile, 'rb')
data = pickle.load(f)
f.close()

while True:
	loginName = input('\033[00;01mUsername: ')
	loginPassword = input('\033[00;01mPassword: \033[8m')
	if loginName == data['userName']