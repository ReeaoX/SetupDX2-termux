#!/usr/bin/env python3

import sys, os, shutil

class files:
	cd = """cd(){
	builtin cd \$*
	LC_COLLATE='C' \\ls -CAw \$COLUMNS --color=always --group-directories-first
	echo
}"""
	md = """md(){
	mkdir -p \"\$@\" && cd \"\$@\"
}"""


HOME = os.getenv('HOME')
DX2FUNCDIR = (HOME + '/.DX2/functions/')
CDFUNC = (DX2FUNCDIR + 'cd.func')
MDFUNC = (DX2FUNCDIR + 'md.func')

if os.path.exists(CDFUNC) == False:
	f = open(CDFUNC, 'w')
	f.write(files.cd)
	f.close()
else:
	print('cd.func already exists')

if os.path.exists(MDFUNC) == False:
	f = open(MDFUNC, 'w')
	f.write(files.cd)
	f.close()
else:
	print('md.func already exists')
