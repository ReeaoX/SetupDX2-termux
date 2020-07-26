#!/usr/bin/env python3

import os
import sys

DIRDX2FUNC = (os.getenv('DX2FUNC') + '/')
DIRDX2AKA = (os.getenv('DX2ALIASES') + '/')

class files:
	cd = (r"""function cd(){
	builtin cd "$*"
	LC_COLLATE='C' \ls --color=always --group-directories-first
	echo
}""")
	ls = (r"""export LS_ARG="--color=always --group-directories-first"

alias {l,ls}="\ls $LS_ARG"
alias ll="ls -l"
alias la="ls -A"
""")


def writefile(x, y, z):
	"""
	writefile(files.cd, DIRDX2FUNC, 'cd.func')
	"""
	TOWRITE = x
	FILENAME = (y + z)
	f = open(FILENAME, 'w')
	f.write(TOWRITE)
	f.close()

