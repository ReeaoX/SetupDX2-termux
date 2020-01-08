#!/usr/bin/env python3

import sys, os, shutil

class files:
	ls = """export LS_OPTS=\"-C -w \\\$COLUMNS --color=always --group-directories-first\"
export LC_COLLATE='C'

alias {ls,LS,l,L}=\"\\ls \$LS_OPTS\"
alias la=\"\ls -A\"
alias ll=\"\\ls -l\"
alias {lla,lal}=\"ls -lA\"

## ls typos
alias {ks,KS}='ls'"""
	git = """alias gc='git clone'
alias gcm='git commit -m'
alias ga='git add'
alias gaa='git add --all'
alias gcob='git checkout -b'
alias gco='git checkout'
alias gstat='git status'
alias gpush='git push -u origin'"""
	misc = """alias n=nano
alias e=echo
alias less='less-r'"""


HOME = os.getenv('HOME')
DX2AKADIR = (HOME + '/.DX2/aliases/')
LSAKA = (DX2AKADIR + 'ls.aka')
GITAKA = (DX2AKADIR + 'git.aka')
MISCAKA = (DX2AKADIR + 'misc.aka')

if os.path.exists(LSAKA) == False:
	f = open(LSAKA, 'w')
	f.write(files.ls)
	f.close()
else:
	print('ls.aka already exists')

if os.path.exists(GITAKA) == False:
	f = open(GITAKA, 'w')
	f.write(files.git)
	f.close()
else:
	print('git.aka already exists')

if os.path.exists(MISCAKA) == False:
	f = open(MISCAKA, 'w')
	f.write(files.misc)
	f.close()
else:
	print('ls.aka already exists')

