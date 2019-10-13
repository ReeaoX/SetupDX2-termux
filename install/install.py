#!/usr/bin/env python3

import os
import shutil
import re

__VERSION__ = '3.0'
HOME = os.getenv('HOME')
DX2 = (HOME + '/.DX2')
DX2BIN = (DX2 + '/bin')
DX2RC = (DX2 + '/rc')
DX2FUNCS = (DX2 + '/functions')
DX2DATA = (DX2 + '/data')
DX2BAK = (DX2 + '/backups')
DX2AKA = (DX2 + '/aliases')
DX2TMP = (DX2 + '/temp')
DX2GIT = (DX2 + '/git')
DX2SHORTCUTS = (DX2 + '/.Shortcuts')
bashrc = (HOME + '/.bashrc')
zshrc = (HOME + '/.zshrc')
loaddx2rc = """
### BEG - LOAD DX2RC ###
if [ -f ~/.dx2rc ]; then
	source ~/.dx2rc;
fi
### END - LOAD DX2RC ###
"""
dx2rc = (HOME + '/.dx2rc')
dx2rx = ("""## Load VARs
#
export DX2=\"$HOME/.DX2\"
export DX2BIN=\"$DX2/bin\"
export DX2FILES=\"$DX2/files\"
export DX2RC=\"$DX2/rc\"
export DX2BAK=\"$DX2/backups\"
export DX2TMP=\"$DX2/temp\"
export DX2GIT=\"$DX2/git\"
export DX2FUNCS=\"$DX2/functions\"
export DX2ALIASES=\"$DX2/aliases\"
export DX2VERSION=""" + str(__VERSION__) + """

## Update PATH
#
if [ $(echo $PATH | grep -qe '.DX2/bin'; echo $?) != 0 ]; then
	export PATH=\"$DX2BIN:$PATH\"
fi

## Load everything in $DX2RC
#
if test "$(ls $DX2RC)" 2&>/dev/null; then
	for RCFILES in $DX2RC/*; do
		if [ -r \"$RCFILES\" ]; then
			source \"$RCFILES\";
		fi
	done
fi

## Load everything in $DX2FUNCS
#
if test "$(ls $DX2FUNCS)" 2&>/dev/null; then
	for FUNCSFILES in $DX2FUNCS/*; do
		if [ -r \"$FUNCSFILES\" ]; then
			source \"$FUNCSFILES\";
		fi
	done
fi
## Load everything in $DX2ALIASES
#
if test "$(ls $DX2ALIASES)" 2&>/dev/null; then
	for ALIASESFILES in $DX2ALIASES/*; do
		if [ -r \"$ALIASESFILES\" ]; then
			source \"$ALIASESFILES\";
		fi
	done
fi
""")

def __createdir(x):
	dir = x
	if os.path.exists(dir) == False:
		print("\033[00;01m[ \033[00;01;38;5;190mWORK \033[00;01m] - Creating Directory \033[00;01;38;5;190m\"\033[00;36m" + str(re.sub(HOME, "~/.", str(dir))) + "\033[00;01;38;5;190m\"\033[00;01m: ", end='')
		os.mkdir(dir)
		print("\r\033[00;01m[ \033[00;01;38;5;46mDONE \033[00;01m]\033[00m")
	else:
		print("Directory \"" + str(dir) + "\" already exists")

# create dirs
__createdir(DX2)
__createdir(DX2BIN)
__createdir(DX2RC)
__createdir(DX2FUNCS)
__createdir(DX2DATA)
__createdir(DX2BAK)
__createdir(DX2AKA)
__createdir(DX2TMP)
__createdir(DX2GIT)
__createdir(DX2SHORTCUTS)

# create dx2rd
dxrc = open(dx2rc, "w")
dxrc.write(dx2rx)
dxrc.close()

# create backups of rc
if os.path.exists(bashrc) == True:
	print("\033[00;38;5;51m~/.bashrc\033[00;01m found !\033[m")
	# CREATE BACKUP
	shutil.copyfile(bashrc, DX2BAK + '/.bashrc')
	f = open(bashrc)
	oldrc = f.read()
	f.close()
	# CHECK FOR EDITS
	if 'source ~/.dx2rc' in oldrc:
		print("\033[00;38;5;51m~/.bashrc\033[00;01m is already set to load \033[00;38;5;51m~/.dx2rc\033[00;01m during boot.\n\nNo additional modification required.\033[00m")
	else:
		# EDIT RC
		print("\033[00;38;5;51m~/.bashrc\033[00;01m doesn't load \033[00;38;5;51m~/.dx2rc\033[00;01m during boot.\n\nEditing file now...\033[00m")
		bash = open(bashrc, "w")
		bash.write(oldrc + loaddx2rc)
		bash.close()
		print('\033[00;01;38;5;46mDONE\033[m')

if os.path.exists(zshrc) == True:
	print("\033[00;38;5;51m~/.zshrc\033[00;01m found !\033[m")
	# CREATE BACKUP
	shutil.copyfile(zshrc, DX2BAK + '/.zshrc')
	f = open(zshrc)
	oldrc = f.read()
	f.close()
	# CHECK FOR EDIT
	if 'source ~/.dx2rc' in oldrc:
		print("\033[00;38;5;51m~/.zshrc\033[00;01m is already set to load \033[00;38;5;51m~/.dx2rc\033[00;01m during boot.\n\nNo additional modification required.\033[00m")
	else:
		# EDIT RC
		print("\033[00;38;5;51m~/.zshrc\033[00;01m doesn't load \033[00;38;5;51m~/.dx2rc\033[00;01m during boot.\n\nEditing file now...\033[00m")
		zsh = open(zshrc, "w")
		zsh.write(oldrc + loaddx2rc)
		zsh.close()
		print('\033[00;01;38;5;46mDONE\033[m')


# edit rc


