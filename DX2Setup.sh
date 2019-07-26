#!/bin/bash

# SCRIPT INFO:
#	-	Vanilla Setup !!
#	-	Script creates all the directories, rc files, and edits
#		.bashrc and/or .zshrc
#	-	It DOES NOT install all the other funxctions / scripts

## STEP 01 - LOAD VARS ##

export DX2="$HOME/.DX2"
export DX2BIN="$DX2/bin"
export DX2FILES="$DX2/files"
export DX2RC="$DX2/rc"
export DX2BAK="$DX2/backups"
export DX2TMP="$DX2/temp"
export DX2GIT="$DX2/git"
export DX2FUNCS="$DX2/functions"
export DX2ALIASES="$DX2/aliases"

## STEP 02 - MAKE DIRS ##

for VARDIRS in {"$DX2","$DX2RC","$DX2BIN","$DX2TMP","$DX2BAK","$DX2GIT","$DX2ALIASES","$DX2FILES"}; do
	if [ ! -d "$VARDIRS" ]; then
		mkdir -p "$VARDIRS";
	fi
done

## STEP 03 - CREATE DX2RC ##

DX2RC_FILE="""
## Load VARs
#
export DX2=\"\$HOME/.DX2\"
export DX2BIN=\"\$DX2/bin\"
export DX2FILES=\"\$DX2/files\"
export DX2RC=\"\$DX2/rc\"
export DX2BAK=\"\$DX2/backups\"
export DX2TMP=\"\$DX2/temp\"
export DX2GIT=\"\$DX2/git\"
export DX2FUNCS=\"\$DX2/functions\"
export DX2ALIASES=\"\$DX2/aliases\"

## Update PATH
#
if [ \$(echo \$PATH | grep -qe '.DX2/bin'; echo \$?) != 0 ]; then
	export PATH=\"\$DX2BIN:\$PATH\"
fi

## Load everything in \$DX2RC
#
for RCFILES in \$DX2RC/*; do
	if [ -r \"\$RCFILES\" ]; then
		. \"\$RCFILES\";
	fi
done

## Load everything in \$DX2FUNCS
#
for FUNCSFILES in \$DX2FUNCS/*; do
	if [ -r \"\$FUNCSFILES\" ]; then
		. \"\$FUNCSFILES\";
	fi
done

## Load everything in \$DX2ALIASES
#
for ALIASESFILES in \$DX2ALIASES/*; do
	if [ -r \"\$ALIASESFILES\" ]; then
		. \"\$ALIASESFILES\";
	fi
done

"""

if [ ! -f "$HOME/.dx2rc" ]; then
	touch "$HOME/.dx2rc"
	echo -e "$DX2RC_FILE" > "$HOME/.dx2rc"
else
	if [ "$(cat "$HOME/.dx2rc" | grep -qe 'DX2 Digital Group'; echo $?)" -eq '0' ]; then
		echo -en """
For some reason, you already have our file, \"~/.dx2rc\". 
Don't know what it's doing there, but it is getting rena-
med to \".dx2rc.bak\", and a new file will be created.

[ Hit any key to continue, or [CTRL + c] to quit ]

"""
		read
		mv "$HOME/.dx2rc" "$HOME/.dx2rc.bak"
		echo -e "$DX2RC_FILE" > "$HOME/.dx2rc"
	fi
fi

unset DX2RC_FILE

## STEP 04 - EDIT RC FILES ##

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


## check for .bashrc first. If it exist, then chances are, .profile
## also exists.
		# .bashrc is being loaded some how, so add the line to
#
if [ -f "$HOME/.bashrc" ]; then
	if [ $(cat "$HOME/.bashrc" | grep -qe 'LOAD .DX2RC'; echo $?) != 0 ]; then
		echo -e "$LOADMYRC" >> "$HOME/.bashrc"
	fi
fi

if [ -f "$HOME/.zshrc" ]; then
	if [ $(cat "$HOME/.profile" | grep -qe 'LOAD .DX2RC'; echo $?) != 0 ]; then
		echo -e "$LOADMYRC" >> "$HOME/.zshrc"
	fi
fi

unset LOADMYRC
