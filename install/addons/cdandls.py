#!/usr/bin/env python3

import os

DX2FUNCS = os.getenv('DX2FUNCS')

cdandls = ("""function cd(){
	builtin cd $*
	LC_COLLATE='C' \ls -A -C -w $COLUMNS --color=always --group-directories-first
	echo
}
""")

f = open(DX2FUNCS + '/cd.funcs', "w")
f.write(cdandls)
f.close()
