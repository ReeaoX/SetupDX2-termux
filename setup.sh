#!/bin/bash

SETUPDIR=$PWD

# VARS:	LOADMYRC
# VALU:	This var is used to edit .bashrc. Its value is what gets
#		added to the file
#
LOADMYRC="""
### BEG - LOAD .DX2RC ###
if [ \"\$DX2DIGITAL\" != 'loaded' ]; then
	if [ -f \"\$HOME/.dx2rc\" ]; then
		. \"\$HOME/.dx2rc\";
	fi
	export DX2DIGITAL='loaded'
fi
### END - LOAD .DX2RC ###
"""



if [ ! -d "$HOME/.DX2" ]; then
	cp -r ./.DX2 "$HOME/"
fi

if [ ! -f "$HOME/.dx2rc" ]; then
	cp ./.dx2rc "$HOME/"
fi


## check for .bashrc first. If it exist, then chances are, .profile
## also exists.
		# .bashrc is being loaded some how, so add the line to
#
if [ -f "$HOME/.bashrc" ]; then
	if [ $(cat "$HOME/.bashrc" | grep -qe 'LOAD .DX2RC'; echo $?) != 0 ]; then
		echo -e "$LOADMYRC" >> "$HOME/.bashrc"
	fi
fi

if [ -f "$HOME/.profile" ]; then
	if [ $(cat "$HOME/.profile" | grep -qe 'LOAD .DX2RC'; echo $?) != 0 ]; then
		echo -e "$LOADMYRC" >> "$HOME/.profile"
	fi
fi

