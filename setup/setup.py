#!/usr/bin/env python3

import os
import time

__VERSION__ = 2.4
INSTALLEDV = None
HOME = os.getenv('HOME')
DXHOME = (HOME + '/.DX2')
DXBIN = (DXHOME + '/bin')
DXRC = (DXHOME + '/rc')
DXDATA = (DXHOME + '/data')
DXBAK = (DXHOME + '/backups')
DXTMP = (DXHOME + '/temp')
DXGIT = (DXHOME + '/git')
DXFUNCS = (DXHOME + '/functions')
DXAKA = (DXHOME + '/aliases')
DXSHORTCUTS = (DXHOME + '/.Shortcuts')
FILEDX2RC = (HOME + '/.dx2rc')
FILEBASHRC = (HOME + '/.bashrc')
FILEZSHRC = (HOME + '/.zshrc')
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
for RCFILES in $DX2RC/*; do
	if [ -r \"$RCFILES\" ]; then
		source \"$RCFILES\";
	fi
done

## Load everything in $DX2FUNCS
#
for FUNCSFILES in $DX2FUNCS/*; do
	if [ -r \"$FUNCSFILES\" ]; then
		source \"$FUNCSFILES\";
	fi
done

## Load everything in $DX2ALIASES
#
for ALIASESFILES in $DX2ALIASES/*; do
	if [ -r \"$ALIASESFILES\" ]; then
		source \"$ALIASESFILES\";
	fi
done""")

### CHECK FOR DX2RC ###
print("[-] CHECKING FOR ~/.dx2rc\n\n")
print("\t\033[00;01m[\033[38;5;190m⏳\033[00;01m]  Locating file (~/.dx2rc)")
if os.path.exists(HOME + '/.dx2rc') == False:
	print("\r \033[00;01m[\033[00;01;38;5;196m✗\033[00;01m]\n\tFile not found\n\n \033[00;01m[\033[38;5;190m⏳\033[00;01m] Creating file\033[m")
	dx2rcfile = open("HOME + '/.dx2rc'", "w")
	dx2rcfile.write(dx2rx)
	dx2rcfile.close()
	print('\r \033[00;01m[\033[00;01;38;5;46m✔\033[00;01m]  \033[00m\n\tFile created\n')
else:
	print("\r \033[00;01m[\033[00;01;38;5;46m✔\033[00;01m]  \033[00m\n\tFile Found !\n")
	print("\nRetrieving and comparing version found on system .")
	INSTALLEDV = os.getenv('DX2VERSION')
	if float(INSTALLEDV) < float(__VERSION__):
		print("Installed version (" + str(INSTALLEDV) + ") is not current - Update is suggested.\n\n")
		dx2rcfile = open("HOME + '/.dx2rc'", "w")
		dx2rcfile.write(dx2rx)
		dx2rcfile.close()
	else:
		print("Installed version (" + str(INSTALLEDV) + ") is current - Update is not required.\n\n")

def __checkdir(x):
	DIRNAME = x
	print('
	if os.path.exists(DIRNAME) == False:
		os.mkdir(DIRNAME)
		del DIRNAME
	

if os.path.exists(HOME + '/.dx2rc') == True:
	INSTALLEDV = os.getenv('DX2VERSION')








