#!/usr/bin/env python3

import os
import re
import shutil

__VERSION__ = '4.2'
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

print('')

class files:
	loaddx2rc = ("""
### BEG - LOAD DX2RC ###
if [ -f ~/.dx2rc ]; then
	. ~/.dx2rc;
fi
### END - LOAD DX2RC ###
""")
	dx2rc = ("""## Load VARs
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

class stringsforfiles:
	modifiedcd = ("""cd(){
	builtin cd $*
	LC_COLLATE='C' \ls -ACw $COLUMNS --color=always --group-directories-first
}""")
	defaultls = ("""export LS_OPTS="-C -w \$COLUMNS --color=always --group-directories-first"
export LC_COLLATE='C'

alias ls="\ls $LS_OPTS"
alias l=ls
alias la='ls -A'
alias ll='ls -l'
alias lla='ls -Al'
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


class addons:
	class bin:
		uninstall = (r"""#!/bin/bash

mv $DX2BAK/.bashrc $HOME/.bashrc
rm $HOME/.dx2rc
rm -rf $HOME/.DX2/
""")
		colormap = (r"""#!/usr/bin/env python3

import sys, os

_VERSION_ = "1.0"

initcount = 0

def cmap():
	print('[00;01mBasic Colors: [m')
	initcount = 0
	count = 7
	while count >= 0:
		print('[m' + str(initcount).zfill(2) + ':[38;5;16;4;48;5;' + str(initcount) + 'm  [m ',end='')
		initcount += 1
		count -= 1
	print('')
	count = 7
	while count >= 0:
		print('[m' + str(initcount).zfill(2) + ':[38;5;16;4;48;5;' + str(initcount) + 'm  [m ',end='')
		initcount += 1
		count -= 1
	print('')
	print('')
	print('[00;01mAdvanced colors: [m')
	initcount = 16
	while initcount < 232:
		countb = 6
		while countb > 0:
			count = 6
			while count > 0:
				print('[m' + str(initcount).zfill(3) + ':[38;5;16;4;48;5;' + str(initcount) + 'm   [m ',end='')
				initcount += 1
				count -= 1
			countb -= 1
			print('')
		print('')
	print('[00;01mShades of grey: [m')
	while initcount < 256:
		count = 6
		while count > 0:
			print('[m   ' + '[' + str(len(str(initcount))) + 'D' + str(initcount) + ':[38;5;16;4;48;5;' + str(initcount) + 'm   [m ',end='')
			initcount += 1
			count -= 1
		print('')


cmap()
""")
	class functions:
		cd = (r"""function cd(){
	builtin cd $*
	LC_COLLATE='C' \ls --color=always --group-directories-first -ALF -w $COLUMNS
	echo
}
""")
	class aliases:
		ls = (r"""export LS_ARG="--color=always --group-directories-first -F"

alias {l,ls}="\ls $LS_ARG -L"
alias {L,LS}="\ls $LS_ARG"
alias LS="\ls $LS_ARG"
alias ll="ls -l"
alias la="ls -A"
""")
		git = (r"""alias gs="git status"
alias gpm="git push -u origin master"
alias gpull="git pull"
alias gcom="git commit -m"
alias gco="git checkout"
alias gcob="git checkout -b"
""")
		misc = (r"""alias lg=lazygit
#alias webserver="python -m SimpleHTTPServer"
""")
		colormap = (r"""alias colormap="colormap | \less -er -P '[46m[38;5;16m  -- [47mHit [42m[[47mPGDN[42m][[47mPGUP[42m][47m to scroll or [41m[[47mQ[41m][47m to quit [46m--[m'"
""")

class funcs:
	def checkdirs(x):
		dirs = str(x)
		shortdir = re.sub(HOME, '~', dirs)
		print(' \033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m Creating \033[38;5;51m' + str(shortdir), end='')
		if os.path.exists(dirs) == True:
			print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')
#			print('\r \033[00;01;38;5;51m[\033[00;01mi\033[00;01;38;5;51m] \033[m')
#			print('\t\033[00;01;32mDirectory already exists.')
		else:
			os.mkdir(dirs)
			print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')
		del dirs

	def detectdx():
		init = int('0')
		print("Checking system for any previous versions of DX2 Setup: ")
		print(' \033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m\tChecking for DX2 vars.', end='')
		if os.getenv('DX2VERSION') is not None:
			print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')
			init = int(init) + int('1')
		else:
			print('\r \033[00;01;38;5;196m[\033[00;01m✖\033[00;01;38;5;196m] \033[m')
			init = int(init) + int('0')
		print(' \033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m\tChecking for DX2 directories.', end='')
		if os.path.exists(HOME + '.DX2') == True:
			print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')
			init = int(init) + int('1')
		else:
			print('\r \033[00;01;38;5;196m[\033[00;01m✖\033[00;01;38;5;196m] \033[m')
#			installyn = '1'
			init = int(init) + int('0')
		print(' \033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m\tChecking for ~/.dx2rc.', end='')
		if os.path.exists(HOME + '/.dx2rc') == True:
			print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')
			init = int(init) + int('1')
		else:
			print('\r \033[00;01;38;5;196m[\033[00;01m✖\033[00;01;38;5;196m] \033[m')
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

class install:
	def installaddons(x, y, z):
		"""
		syntax: installaddons(addons.bin.colormap, DX2BIN, 'colormap.aka')
		"""
		FILE = x
		DIR = y
		FILENAME = z
		PATH = (DIR + '/' + FILENAME)
		f = open(PATH, 'w')
		f.write(FILE)
		f.close()
	def dirs():
		tools.subtitle('Setting up directories:')
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
		tools.subtitle('Creating ~/.dx2rc')
		print(' \033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m Creating \033[38;5;51m~/.dx2rc', end='')
		f = open(HOME + '/.dx2rc', "w")
		f.write(files.dx2rc)
		f.close()
		print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')
	def bakbashrc():
		'''
		If ~/.bashrc is found, copy the file into $DX2BAK
		'''
		SHELLRC = (HOME + '/.bashrc')
		if os.path.exists(SHELLRC) == True:
			shutil.copyfile(SHELLRC, DX2BAK + '/.bashrc')
	def editbashrc():
		'''
		Checks to see if .bashrc has been edited to load .dx2rc or
		not. If not, create a new file with the old .bashrc files
		with the bit to load dx2rc at the end.
		'''
		SHELLRC = (HOME + '/.bashrc')
		f = open(SHELLRC,"r")
		bashrcfile = f.read()
		f.close()
		if files.loaddx2rc not in bashrcfile:
			f = open(SHELLRC, "w")
			f.write(bashrcfile + files.loaddx2rc)
			f.close()



	def editshellrc():
		install.bakbashrc()
		install.editbashrc()
#		tools.subtitle('Editing Shells rc file')
#		print(' \033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m Detecting Shell', end='')
#		if os.getenv('BASH') is not None:
#			SHELL = 'bash'
#			SHELLRC = (HOME + '/.' + str(SHELL) + 'rc')
#		elif os.getenv('ZSH') is not None:
#			SHELL = 'zsh'
#			SHELLRC = (HOME + '/.' + str(SHELL) + 'rc')
#		else:
#			print('Shell not found')

	def copyuninstall():
		f = open((DX2BIN + '/dx2-uninstall'), 'w')
		f.write(addons.bin.uninstall)
		f.close()
		os.chmod((DX2BIN + '/dx2-uninstall'), 0o766)

	def install():
		tools.titlebar('DX2 Setup', 'bg', 'fg')
		install.dirs()
		install.dx2rc()
		install.copyuninstall()
		install.editshellrc()



#\033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m
#\r\033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m]\033[m
#\r\033[00;01;38;5;196m[\033[00;01m✖\033[00;01;38;5;196m]\033[m

#funcs.detectdx()
install.install()
<<<<<<< HEAD


=======
#
#
#def auto():
#	"""
#		FIRST SUB
#	"""
#	init = 0
#	print(WAIT + 'TESTING ONE')
#	init = init + 1
#	print('\t' + WAIT + 'TESTING SUB A', end='')
#	time.sleep(1)
#	print('\r\t' + DONE)
#	init = init + 1
#	print('\t' + WAIT + 'TESTING SUB B', end='')
#	time.sleep(1)
#	print('\r\t' + DONE)
#	init = init + 1
#	print('\t' + WAIT + 'TESTING SUB C', end='')
#	time.sleep(1)
#	print('\r\t' + DONE)
#	print('\033[' + str(init + 1) + 'A\r' + DONE + '\033[' + str(init) + 'B')
#	"""
#		SECOND SUB
#	"""
#	init = 0
#	
#
#auto()
>>>>>>> 7386154010b9ccd214b88f0e7aaa15c741fc89cd
