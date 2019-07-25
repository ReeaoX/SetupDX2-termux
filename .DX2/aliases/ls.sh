#!/bin/bash

#export DEFAULT_OPTS_LS="-C -w $COLUMNS -F --color=always --group-directories-first"

alias {ls,LS,l,L}="\ls -C -w $COLUMNS -F --color=always --group-directories-first"
#alias l="\ls -C -w $COLUMNS -F --color=always --group-directories-first"
alias la="\ls -a -C -w $COLUMNS -F --color=always --group-directories-first"
alias ll="\ls -l -C -w $COLUMNS -F --color=always --group-directories-first"
alias {ks,KS}='ls'

