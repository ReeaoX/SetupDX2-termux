#STEPS

# STEP1 - LOAD VARS
export DX2="$HOME/.DX2"
export DX2BIN="$DX2/bin"
export DX2DATA="$DX2/data"
export DX2RC="$DX2/rc"
export DX2BAK="$DX2/backups"
export DX2TMP="$DX2/temp"
export DX2GIT="$DX2/git"
export DX2FUNCS="$DX2/functions"
export DX2ALIASES="$DX2/aliases"
export DX2SHORTCUTS="$DX2/.Shortcuts"

# STEP2 - CHECK FOR ~/.dx2rc
__check_dx2rc

# STEP3 - CHECK/MKDIR FOR DIRS
__check_dir "$DX2"
__check_dir "$DX2BIN"
__check_dir "$DX2DATA"
__check_dir "$DX2RC"
__check_dir "$DX2BAK"
__check_dir "$DX2TMP"
__check_dir "$DX2GIT"
__check_dir "$DX2FUNCS"
__check_dir "$DX2ALIASES"
__check_dir "$DX2SHORTCUTS"

# STEP4 - EDIT BASHRC OR ZSHRC
if [ -f ~/.bashrc ]; then
	if [ "$(cat ~/.bashrc | grep -qe 'source ~/.dx2rc'; echo $?)" != 0 ]; then
		echo -en """
if [ -f ~/.dx2rc ]; then
	source ~/.dx2rc;
fi
""" >> ~/.bashrc;
	fi
fi

if [ -f ~/.zshrc ]; then
	if [ "$(cat ~/.zshrc | grep -qe 'source ~/.dx2rc'; echo $?)" != 0 ]; then
		echo -en """
if [ -f ~/.dx2rc ]; then
	source ~/.dx2rc;
fi
""" >> ~/.zshrc;
	fi
fi

