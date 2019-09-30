__DXVERSION__=2.1       # This should be loaded in the main setup script


### FUNCTION - __check_dx2rc() ###
function __check_dx2rc(){
	echo -en """
Checking for the file ~/.dx2rc ...

""";
	if [ ! -f ~/.dx2rc ]; then
		echo -e """The file '~/.dx2rc' could not be located.

Creating the file now...

[ HIT ANY KEY TO CONTINUE ]

""";
		read;
		echo "$dx2rcfile" > ~/.dx2rc;
	else
		echo =en """
The file '~/.dx2rc' was found.

[ HIT ANY KEY TO CONTINUE ]

""";
		read;
	fi
}

### FUNCTION - __check_dir() ###
function __check_dir(){
	DIR2CHK=$1
	if [ ! -d "$DIR2CHK" ]; then
		mkdir -p "$DIR2CHK";
	fi
	unset DIR2CHK;
}

## FILES - DX2RC##
dx2rcfile="""## Load VARs
#
export DX2=\"\$HOME/.DX2\"
export DX2VERSION="$__DXVERSION__"
export DX2BIN=\"\$DX2/bin\"
export DX2DATA=\"\$DX2/data\"
export DX2RC=\"\$DX2/rc\"
export DX2BAK=\"\$DX2/backups\"
export DX2TMP=\"\$DX2/temp\"
export DX2GIT=\"\$DX2/git\"
export DX2FUNCS=\"\$DX2/functions\"
export DX2ALIASES=\"\$DX2/aliases\"
export DX2SHORTCUTS=\"\$DX2/.Shortcuts\"


## Load everything in \$DX2FUNCS
#
if [ \"\$(ls \$DX2FUNCS | wc -l)\" != 0 ]; then
	for FUNCSFILES in \$DX2FUNCS/*; do
		if [ -r \"\$FUNCSFILES\" ]; then
			source \"\$FUNCSFILES\";
		fi
	done
fi

## Load everything in \$DX2RC
#
if [ \"\$(ls \$DX2RC | wc -l)\" != 0 ]; then
	for RCFILES in \$DX2RC/*; do
		if [ -r \"\$RCFILES\" ]; then
			source \"\$RCFILES\";
		fi
	done
fi


## Load everything in \$DX2ALIASES
#
if [ \"\$(ls \$DX2ALIASES | wc -l)\" != 0 ]; then
	for ALIASESFILES in \$DX2ALIASES/*; do
		if [ -r \"\$ALIASESFILES\" ]; then
			source \"\$ALIASESFILES\";
		fi
	done
fi

if [ \"\$(echo \$PATH | grep -qe '.DX2/bin'; echo \$?)\" != '0' ]; then
	export PATH=\"\$DX2BIN:\$PATH\";
fi

export CDPATH=~/.Shortcuts"""

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

clear
unset -f __check_dir __check_dx2rc
test -f $HOME/.dx2rc && echo '.dx2rc found'; source $HOME/.dx2rc || echo 'missing .dx2rc'
test -d $DX2 && echo '\$DX2 found' || echo '$DX2 not found'
