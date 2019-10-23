#!/usr/bin/env python3

import os
import re
import shutil

__VERSION__ = '4.0'
COLS, LINES = shutil.get_terminal_size()
HOME = os.getenv('HOME')
installyn = None

## DX2 VARS
DX2 = (HOME + '/.DX2')
DX2BIN = (DX2 + '/bin')
DX2RC = (DX2 + '/rc')
DX2DATA = (DX2 + '/data')
DX2FUNCS = (DX2 + '/functions')
DX2BAK = (DX2 + '/backups')
DX2TMP = (DX2 + '/temp')
DX2GIT = (DX2 + '/git')
DX2AKA = (DX2 + '/aliases')
DX2SHORTCUTS = (DX2 + '/.Shortcuts')
ICONWAIT = ' \033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m'
ICONCHECK = ' \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m'
ICONX = ' \033[00;01;38;5;196m[\033[00;01m✖\033[00;01;38;5;196m] \033[m'
loaddx2rc = ("""
### BEG - LOAD DX2RC ###
if [ -f ~/.dx2rc ]; then
    source ~/.dx2rc;
fi
### END - LOAD DX2RC ###
""")
dx2rcfile = ("""## Load VARs
#
export DX2="$HOME/.DX2"
export DX2VERSION=""" + '"' + str(__VERSION__) + '"' + """
export DX2BIN="$DX2/bin"
export DX2DATA="$DX2/data"
export DX2RC="$DX2/rc"
export DX2BAK="$DX2/backups"
export DX2TMP="$DX2/temp"
export DX2GIT="$DX2/git"
export DX2FUNCS="$DX2/functions"
export DX2ALIASES="$DX2/aliases"
export DX2SHORTCUTS="$DX2/.Shortcuts"


## Load everything in $DX2FUNCS
#
if [ "$(ls $DX2FUNCS | wc -l)" != 0 ]; then
	for FUNCSFILES in $DX2FUNCS/*; do
		if [ -r "$FUNCSFILES" ]; then
			source "$FUNCSFILES";
		fi
	done
fi

## Load everything in $DX2RC
#
if [ "$(ls $DX2RC | wc -l)" != 0 ]; then
	for RCFILES in $DX2RC/*; do
		if [ -r "$RCFILES" ]; then
			source "$RCFILES";
		fi
	done
fi


## Load everything in $DX2ALIASES
#
if [ "$(ls $DX2ALIASES | wc -l)" != 0 ]; then
	for ALIASESFILES in $DX2ALIASES/*; do
		if [ -r "$ALIASESFILES" ]; then
			source "$ALIASESFILES";
		fi
	done
fi

if [ "$(echo $PATH | grep -qe '.DX2/bin'; echo $?)" != '0' ]; then
	export PATH="$DX2BIN:$PATH";
fi

export CDPATH=~/.Shortcuts
""")


class tools():
	def titlebar(x, y, z):
		TITLE = str(x)
		BG = str(y)
		FG = str(z)
		if BG == 'bg':
			BG = ('\033[00;01;48;5;196m')
		else:
			BG = ('\033[00;01;48;5;' + str(y) + 'm')
		if FG == 'fg':
			FG = ('\033[38;5;15m')
		else:
			FG = ('\033[38;5;' + str(z) + 'm')
		print('\033c' + BG + FG + ' ' * COLS + '\r ' + str(TITLE) + '\033[m\n')
		del BG, FG, TITLE
	def subtitle(x):
		subtitle = str(x)
		print('\n\033[00;01;38;5;196m[\033[00;01m-\033[00;01;38;5;196m]\033[00;01m - ' + str(subtitle) + '\033[m')
		del subtitle



class funcs():
	def checkdirs(x):
		dirs = str(x)
		shortdir = re.sub(HOME, '~', dirs)
		print(ICONWAIT + ' Creating \033[38;5;51m' + str(shortdir), end='')
		if os.path.exists(dirs) == True:
			print('\r' + ICONCHECK)
#			print('\r \033[00;01;38;5;51m[\033[00;01mi\033[00;01;38;5;51m] \033[m')
#			print('\t\033[00;01;32mDirectory already exists.')
		else:
			os.mkdir(dirs)
			print('\r' + ICONCHECK)
		del dirs

	def detectdx():
		init = int('0')
		print("Checking system for any previous versions of DX2 Setup: ")
		print(ICONWAIT + '\tChecking for DX2 vars.', end='')
		if os.getenv('DX2VERSION') is not None:
			print('\r' + ICONCHECK)
			init = int(init) + int('1')
		else:
			print('\r' + ICONX)
			init = int(init) + int('0')
		print(ICONWAIT + '\tChecking for DX2 directories.', end='')
		if os.path.exists(HOME + '.DX2') == True:
			print('\r' + ICONCHECK)
			init = int(init) + int('1')
		else:
			print('\r' + ICONX)
#			installyn = '1'
			init = int(init) + int('0')
		print(ICONWAIT + '\tChecking for ~/.dx2rc.', end='')
		if os.path.exists(HOME + '/.dx2rc') == True:
			print('\r' + ICONCHECK)
			init = int(init) + int('1')
		else:
			print('\r' + ICONX)
#			installyn = '1'
			init = int(init) + int('0')
		if init == int('0'):
			print('\nDX2 was not found')
			funcs.asktoinstall()
		elif init == int('3'):
			print('\nDX2 detected / installed')
		else:
			print('\nDX2 found, but some elements are missing')
			funcs.asktoinstall()

	def asktoinstall():
		ans = input("""
Do you want to install DX2 now?
[Y/n]: """)
		if ans == 'y':
			print('installing...')
		elif ans == 'Y':
			print('installing...')
		elif ans == '':
			print('installing...')
		elif ans == 'n':
			print('exiting...')
		elif ans == 'N':
			print('exiting...')

class install():
	def dirs():
		tools.subtitle('Setting up DX2 directories:')
		funcs.checkdirs(DX2)
		funcs.checkdirs(DX2RC)
		funcs.checkdirs(DX2BIN)
		funcs.checkdirs(DX2DATA)
		funcs.checkdirs(DX2FUNCS)
		funcs.checkdirs(DX2BAK)
		funcs.checkdirs(DX2TMP)
		funcs.checkdirs(DX2GIT)
		funcs.checkdirs(DX2SHORTCUTS)
		funcs.checkdirs(DX2AKA)
	def dx2rc():
		tools.subtitle('Creating DX2 startup file(s):')
		print(ICONWAIT + ' Creating \033[38;5;51m~/.dx2rc', end='')
#		if os.path.exists(HOME + '/.dx2rc') == True:
#			print('\r \033[00;01;38;5;51m[\033[00;01mi\033[00;01;38;5;51m] \033[m')
#			print('\t\033[00;01;32mDirectory already exists.')
#		else:
		f = open(HOME + '/.dx2rc', "w")
		f.write(dx2rcfile)
		f.close()
		print('\r' + ICONCHECK)

	def editshellrc():
		tools.subtitle('Editing startup file(s) to load DX2 files')
		print(ICONWAIT + ' Detecting Shell', end='')
		if os.getenv('BASH') is not None:
			SHELL = 'bash'
			SHELLRC = (HOME + '/.' + str(SHELL) + 'rc')
			print('\033[00;01;38;5;46m Found \033[m- \033[00;01;48;5;21m $' + str.upper(SHELL) + ' \033[m\r' + ICONCHECK)
		elif os.getenv('ZSH') is not None:
			SHELL = 'zsh'
			SHELLRC = (HOME + '/.' + str(SHELL) + 'rc')
			print('\033[00;01;38;5;46m Found \033[m- \033[00;01;48;5;21m $' + str.upper(SHELL) + ' \033[m\r' + ICONCHECK)
		else:
			print('Shell not found' + '\r' + ICONX)
		print('\t' + ICONWAIT + ' Searching for \033[00;38;5;51m' + str(SHELLRC) + '\033[00;01m: \033[m', end='')
        # if shellrc file exists:
		if os.path.exists(SHELLRC) == True:
		    print('\033[00;01;38;5;46mFound\033[m\r\t' + ICONCHECK)
		    print('\t' + ICONWAIT + ' Creating backup: ', end='')
		    shutil.copyfile(SHELLRC, DX2BAK + '/.' + str(SHELL) + 'rc')
		    print('\033[00;01;38;5;46m DONE \033[m\r\t' + ICONCHECK)
        # if shellrc does NOT exist
		else:
	        print('\033[00;01;38;5;196mNot Found\033[m\r\t' + ICONX)
            print('\t' + ICONWAIT + " Creating file: ", end='')
            f = open(SHELLRC, "w")
            f.write(loaddx2rc)
            f.close()
            print('\033[00;01;38;5;46m DONE \033[m\r\t' + ICONCHECK)


	def install():
		tools.titlebar('DX2 Setup', 'bg', 'fg')
		install.dirs()
		install.dx2rc()
		install.editshellrc()



#\033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m
#\r\033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m]\033[m
#\r\033[00;01;38;5;196m[\033[00;01m✖\033[00;01;38;5;196m]\033[m

#funcs.detectdx()
install.install()
