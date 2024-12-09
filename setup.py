#!/data/data/com.termux/files/usr/bin/python3
ImportError_message = "To setup DX2 runtime, Python modules is required."

try:
  from decouple import config as conf
  from rich.prompt import Confirm as ryn
  from dotenv import find_dotenv as dotfind, load_dotenv as dotload
  from os import mkdir as mkPath
  from pathlib import Path as pydir, PurePath as puredir
  from click import clear as cls
  import re
  from shutil import copy2 as pycopy
except ImportError:
  raise ImportError(ImportError_message)

"""Load '.env'-formatted config (with 'dotenv')."""
dotenv_file = ("dx%s" % "2" + "-" + "config" + ".%s" % "env") # identified as "dx2-config.env".
dotload(dotfind(dotenv_file))

__VERSION__ = conf("DX2_PYTHON_SCRIPT_VERSION")
COLUMN = conf("COLUMNS")
LINES = conf("LINES")
PREFIX = conf("PREFIX", default="/")
SHELL = conf("SHELL")
PREFIX_ETC = puredir(PREFIX, "etc")
PREFIX_BIN = puredir(PREFIX, "bin")
HOME = conf("HOME", default="/root")
installyn = None

"""DX2 variables(?)."""
DX2 = conf("DX2")
DX2BIN = conf("DX2BIN")
DX2RC = conf("DX2RC")
DX2DATA = conf("DX2DATA")
DX2RC_RUNTIME = conf("DX2RC_RUNTIME")
DX2FUNCS = conf("DX2FUNCS")
DX2BAK = conf("DX2BAK")
DX2ALIASES = conf("DX2ALIASES", default="{0}/.dx2-aliases".format(HOME))
DX2TMP = conf("DX2TMP")
DX2GIT = conf("DX2GIT")
modifiedcd_function_name = "cd"
DX2_CDPATH = conf("DX2_CDPATH")
DX2AKA = conf("DX2AKA")
DX2SHORTCUTS = conf("DX2SHORTCUTS")

cls()

"""The 'files' recursive class."""
class files:
	loaddx2rc = ("""if [[ -f {0} ]]; then
	source {0};
fi""".format(DX2RC_RUNTIME))
	dx2rc = ("""export DX2="{DX2}"
export DX2VERSION=""" + '"%s"' % str(__VERSION__) + """
export DX2BIN="{0}"
export DX2DATA="{1}"
export DX2RC="{2}"
export DX2BAK="{3}"
export DX2TMP="{4}"
export DX2GIT="{5}"
export DX2FUNCS="{6}"
export DX2ALIASES="{7}"
export DX2SHORTCUTS="{8}"
""".format(DX2BIN, DX2BIN, DX2DATA, DX2RC, DX2BAK, DX2TMP, DX2GIT, DX2ALIASES, DX2SHORTCUTS) + """
if [[ -n "$(ls $DX2FUNCS)" ]]; then
	for FUNCSFILES in $DX2FUNCS/*; do
		if [[ -r "$FUNCSFILES" ]]; then
			source "$FUNCSFILES";
		fi
	done
fi
""" + """
if [[ -n "$(ls $DX2RC)" ]]; then
	for RCFILES in $DX2RC/*; do
		if [[ -r "$RCFILES" ]]; then
			source "$RCFILES";
		fi
	done
fi
""" + """
if [[ -n "$(ls $DX2ALIASES)" ]]; then
	for ALIASESFILES in $DX2ALIASES/*; do
		if [ -r "$ALIASESFILES" ]; then
			source "$ALIASESFILES";
		fi
	done
fi
""" + """
if [ "$(echo $PATH | grep -qe '.DX2/bin'; echo $?)" != '0' ]; then
	export PATH+=":$DX2BIN";
fi
""" + """
export CDPATH=%s""" % DX2_CDPATH)

class stringsforfiles:
	modifiedcd = ("""function %s () {
	builtin %s $*
	LC_COLLATE='C' \ls -ACw $COLUMNS --color=always --group-directories-first
}""" % modifiedcd_function_name)
	defaultls = ("""export LS_OPTS="-C -w \$COLUMNS --color=always --group-directories-first"
export LC_COLLATE='C'
""" + """
alias ls="\ls $LS_OPTS"
alias l=ls
alias la='ls -A'
alias ll='ls -l'
alias lla='ls -Al'""")

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

class funcs:
	def checkdirs(x):
		dirs = str(x)
		shortdir = re.sub(HOME, '~', dirs)
		print('\033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m Creating \033[38;5;51m' + str(shortdir), end='')

		if pydir(dirs).exists() == True:
                        print('\r \033[00;01;38;5;46m[\033[00;01m✓\033[00;01;38;5;46m] \033[m')
                        # print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')
                        # print('\r \033[00;01;38;5;51m[\033[00;01mi\033[00;01;38;5;51m] \033[m')
                        # print('\t\033[00;01;32mDirectory already exists.')
		elif pydir(dirs).exists() == False:
			mkPath(dirs)
                        print('\r \033[00;01;38;5;46m[\033[00;01m✓\033[00;01;38;5;46m] \033[m')
			# print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')
		del dirs

	def detectdx():
		init = int('0')
		print("Checking system for any previous versions of DX2 Setup: ")
		print('\n\033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m\tChecking for DX2 vars.', end='')

                DX2_detectdx_LOCATE = puredir(HOME, ".DX2")
                DX2_detectdx_LOCATE_STR = str(DX2_detectdx_LOCATE)
                dx2rc_detectdx_LOCATE = puredir(HOME, ".dx2rc")
                dx2rc_detectdx_LOCATE_STR = str(dx2rc_detectdx_LOCATE)

		if conf("DX2VERSION") is not None:
			print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')
			init = int(init) + int('1')
		elif conf("DX2VERSION") is None:
			print('\r \033[00;01;38;5;196m[\033[00;01m✖\033[00;01;38;5;196m] \033[m')
			init = int(init) + int('0')

		print('\033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m\tChecking for DX2 directories.', end='')
		if pydir(DX2_detectdx_LOCATE_STR).exists() == True:
			print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')
			init = int(init) + int('1')
		elif pydir(DX2_detectdx_LOCATE_STR).exists() == False:
			print('\r \033[00;01;38;5;196m[\033[00;01m✖\033[00;01;38;5;196m] \033[m')
                        # installyn = '1'
			init = int(init) + int('0')

		print('\033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m\tChecking for ~/.dx2rc.', end='')
		if pydir(dx2rc_detectdx_LOCATE_STR).exists() == True:
			print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')
			init = int(init) + int('1')
		elif pydir(dx2rc_detectdx_LOCATE_STR).exists() == False:
			print('\r \033[00;01;38;5;196m[\033[00;01m✖\033[00;01;38;5;196m] \033[m')
                        # installyn = '1'
			init = int(init) + int('0')

		if init == int('0'):
			print("\nDX2 was not found", end="\r\n")
			funcs.asktoinstall()
		elif init == int('3'):
			print("\nDX2 detected / installed", end="\r\n")
		elif not init == int('3'):
			print("\nDX2 found, but some elements are missing", end="\r\n")
			funcs.asktoinstall()

	def asktoinstall():
		ans = ryn.ask("Do you need installing DX2?")

		if ans == "y":
			print("Installing...")
		elif ans == "n":
			rsys.exit("Exiting...")

class funcs_extra:
	def dirs():
		tools.subtitle("Setting up directories:")
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
		tools.subtitle("Creating ~/.dx2rc")
		print('\033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m Creating \033[38;5;51m~/.dx2rc', end='')
                f_dir = puredir(HOME, ".dx2rc")

                if not str(f_dir) == ("%s/.dx2rc" % HOME):
                   f_dir = puredir(HOME, "/", ".dx2src")

		with open(str(f_dir), "w") as f:
		     f.write(files.dx2rc)
                     f.flush()
		print('\r \033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m] \033[m')

	def bak_shellrc():
		"""If ~/.bashrc is found, copy the file into $DX2BAK"""
                PREFIX_BIN_STR = str(PREFIX_BIN)
                SHELL_FORMAT == SHELL.split(PREFIX_BIN_STR + "/")[1]
                PREFIX_ETC_STR = str(PREFIX_ETC)

                if SHELL_FORMAT == "bash":
                   if pydir("%s/.bashrc" % HOME).exists() == True:
		      SHELLRC = puredir(HOME, ".bashrc")
                   elif pydir("%s/.bashrc" % HOME).exists() == False:
                      SHELLRC = puredir(PREFIX_ETC_STR, "bash.bashrc")
                elif SHELL_FORMAT == "xonsh":
                   if pydir("%s/.config" % HOME + "/" + SHELL_FORMAT + "/" + "%s.xsh" % "rc").exists() == True:
                      SHELLRC = puredir(HOME, ".config", SHELL_FORMAT, ("%s.xsh" % "rc"))
                   elif pydir("%s/.config" % HOME + "/" + SHELL_FORMAT + "/" + "%s.xsh" % "rc").exists() == False:
                      SHELLRC = puredir(HOME, ".xonshrc")
                elif not SHELL_FORMAT == "xonsh":
                   SHELLRC = puredir(HOME, (".%src" % SHELL_FORMAT))

                SHELLRC_STR = str(SHELLRC)
		if pydir(SHELLRC_STR).exists() == True:
                   pycopy(SHELLRC, [str(DX2_SHELLRC) for DX2_SHELLRC in puredir(DX2BAK, (".%src" % SHELL_FORMAT))])

	def editbashrc():
		"""Checks to see if .bashrc has been edited to load .dx2rc or
		not. If not, create a new file with the old .bashrc files
		with the bit to load dx2rc at the end."""
		PREFIX_BIN_STR = str(PREFIX_BIN)
                SHELL_FORMAT == SHELL.split(PREFIX_BIN_STR + "/")[1]
                PREFIX_ETC_STR = str(PREFIX_ETC)

                if SHELL_FORMAT == "bash":
                   if pydir("%s/.bashrc" % HOME).exists() == True:
                      SHELLRC = puredir(HOME, ".bashrc")
                   elif pydir("%s/.bashrc" % HOME).exists() == False:
                      SHELLRC = puredir(PREFIX_ETC_STR, "bash.bashrc")
                elif SHELL_FORMAT == "xonsh":
                   if pydir("%s/.config" % HOME + "/" + SHELL_FORMAT + "/" + "%s.xsh" % "rc").exists() == True:
                      SHELLRC = puredir(HOME, ".config", SHELL_FORMAT, ("%s.xsh" % "rc"))
                   elif pydir("%s/.config" % HOME + "/" + SHELL_FORMAT + "/" + "%s.xsh" % "rc").exists() == False:
                      SHELLRC = puredir(HOME, ".xonshrc")
                elif not SHELL_FORMAT == "xonsh":
                   SHELLRC = puredir(HOME, (".%src" % SHELL_FORMAT))

                SHELLRC_STR = str(SHELLRC)
		with open(SHELLRC, "r") as shell_content
		     bashrcfile = shell_content.read()

		if files.loaddx2rc not in bashrcfile:
                        with open(SHELLRC, "w") as shell_content_2:
			     shell_content_2.write(bashrcfile + files.loaddx2rc)
			     shell_content_2.flush()

	def editshellrc():
		funcs_extra.bakbashrc()
		funcs_extra.editbashrc()
                # tools.subtitle('Editing Shells rc file')
                # print(' \033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m Detecting Shell', end='')
                # if os.getenv('BASH') is not None:
                # SHELL = 'bash'
                # SHELLRC = (HOME + '/.' + str(SHELL) + 'rc')
                # elif os.getenv('ZSH') is not None:
                #	SHELL = 'zsh'
                #	SHELLRC = (HOME + '/.' + str(SHELL) + 'rc')
                # else:
                #	print('Shell not found')

	def install():
		tools.titlebar('DX2 Setup', 'bg', 'fg')
		funcs_extra.dirs()
		funcs_extra.dx2rc()
		funcs_extra.editshellrc()

#\033[00;01;38;5;190m[\033[00;01m⌛\033[00;01;38;5;190m]\033[m
#\r\033[00;01;38;5;46m[\033[00;01m✔\033[00;01;38;5;46m]\033[m
#\r\033[00;01;38;5;196m[\033[00;01m✖\033[00;01;38;5;196m]\033[m

#funcs.detectdx()
funcs_extra.install()
