#!/usr/bin/env python3

# CONSTANTS
import os
import shutil
import re

class vars():
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
	
COLS, LINES = shutil.get_terminal_size()

class setupfuncs():
	def createdir(x):
		dir = x
		if os.path.exists(dir) == False:
			print("\033[00;01m[ \033[00;01;38;5;190mWORK \033[00;01m] - Creating Directory \033[00;01;38;5;190m\"\033[00;36m" + str(re.sub(vars.HOME, "~/.", str(dir))) + "\033[00;01;38;5;190m\"\033[00;01m: ", end='')
			os.mkdir(dir)
			print("\r\033[00;01m[ \033[00;01;38;5;46mDONE \033[00;01m]\033[00m")
		else:
			print("Directory \"" + str(dir) + "\" already exists")

	def install():
		# create dirs
		setupfuncs.createdir(vars.DX2)
		setupfuncs.createdir(vars.DX2BIN)
		setupfuncs.createdir(vars.DX2RC)
		setupfuncs.createdir(vars.DX2FUNCS)
		setupfuncs.createdir(vars.DX2DATA)
		setupfuncs.createdir(vars.DX2BAK)
		setupfuncs.createdir(vars.DX2AKA)
		setupfuncs.createdir(vars.DX2TMP)
		setupfuncs.createdir(vars.DX2GIT)
		setupfuncs.createdir(vars.DX2SHORTCUTS)

###############
# create dx2rd
dxrc = open(vars.dx2rc, "w")
dxrc.write(vars.dx2rx)
dxrc.close()

# create backups of rc
if os.path.exists(vars.bashrc) == True:
	print("\033[00;38;5;51m~/.bashrc\033[00;01m found !\033[m")
	# CREATE BACKUP
	shutil.copyfile(vars.bashrc, vars.DX2BAK + '/.bashrc')
	f = open(vars.bashrc)
	oldrc = f.read()
	f.close()
	# CHECK FOR EDITS
	if 'source ~/.dx2rc' in oldrc:
		print("\033[00;38;5;51m~/.bashrc\033[00;01m is already set to load \033[00;38;5;51m~/.dx2rc\033[00;01m during boot.\n\nNo additional modification required.\033[00m")
	else:
		# EDIT RC
		print("\033[00;38;5;51m~/.bashrc\033[00;01m doesn't load \033[00;38;5;51m~/.dx2rc\033[00;01m during boot.\n\nEditing file now...\033[00m")
		bash = open(vars.bashrc, "w")
		bash.write(oldrc + vars.loaddx2rc)
		bash.close()
		print('\033[00;01;38;5;46mDONE\033[m')

if os.path.exists(vars.zshrc) == True:
	print("\033[00;38;5;51m~/.zshrc\033[00;01m found !\033[m")
	# CREATE BACKUP
	shutil.copyfile(vars.zshrc, vars.DX2BAK + '/.zshrc')
	f = open(vars.zshrc)
	oldrc = f.read()
	f.close()
	# CHECK FOR EDIT
	if 'source ~/.dx2rc' in oldrc:
		print("\033[00;38;5;51m~/.zshrc\033[00;01m is already set to load \033[00;38;5;51m~/.dx2rc\033[00;01m during boot.\n\nNo additional modification required.\033[00m")
	else:
		# EDIT RC
		print("\033[00;38;5;51m~/.zshrc\033[00;01m doesn't load \033[00;38;5;51m~/.dx2rc\033[00;01m during boot.\n\nEditing file now...\033[00m")
		zsh = open(vars.zshrc, "w")
		zsh.write(oldrc + vars.loaddx2rc)
		zsh.close()
		print('\033[00;01;38;5;46mDONE\033[m')


# edit rc


############################
class menutools():
	def TITLE(x):
		Title = str(x)
		print('\033c\033[00;01;41m\033[37m' + ' ' * COLS + '\r ' + str(Title) + '\033[m\n')
		del Title


class menus():
	def main():
		menutools.TITLE('Main menu')
		print('hello')


menus.main()

