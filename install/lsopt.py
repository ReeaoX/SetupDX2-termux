#/usr/bin/env python3

import os

defaultls = ("""export LS_OPT="-C -w \$COLUMNS --color=always --group-directories-first"

alias ls="LC_COLLATE='C' \ls "$LS_OPT""
alias l=ls
alias la="ls -A"
alias ll="ls -l | more -d"
alias lla="ls -lA | more -d"
alias lal="ls -lA | more -d"
alias ld="ls -Ad {.*/,*/}"
alias lld="ls -Ald {.*/,*/} | more -d"
alias ldl="ls -Ald {.*/,*/} | more -d"
""")

HOME = os.getenv('HOME')
DX2AKA = (HOME + '/.DX2/aliases')
lsaka = (DX2AKA + '/ls.aka')

f = open(lsaka, "w")
f.write(defaultls)
f.close()
