function __check_dir(){
	DIR2CHK=$1
	echo -en """ \033[00;01m[\033[38;5;190m🔍 \033[00;01m]  \033[00;01mChecking dir \033[36m"$DIR2CHK"\033[00;01m "
	sleep .4
	if [ ! -d "$DIR2CHK" ]; then
		echo -en """\r \033[00;01m[\033[00;01;38;5;196m✗\033[00;01m]\n\tCreating directory: \t\033[m"""
		sleep .4
		mkdir -p "$DIR2CHK"
		echo -en "\033[00;01m[\033[00;01;32mDONE\033[00;01m]\n\n"
	else
		echo -en "\r \033[00;01m[\033[00;01;38;5;46m✔\033[00;01m] \033[00m\n"
	fi
	unset DIR2CHK;
}

__DXVERSION__=2.4

### CHECK FOR DX2 ###
__DXTITLE "DX2 Setup"
echo -en "\033[00;01m[\033[38;5;196m-\033[00;01m] CHECKING SYSTEM FOR DX2 SETUP\033[m\n"
echo -en """ \033[00;01m[\033[38;5;190m🔍 \033[00;01m]  \033[00;01mSearching system\033[00;01m "
if [ $DX2VERSION ]; then
	echo -en "\r \033[00;01m[\033[00;01;38;5;46m✔\033[00;01m] \033[00m\n\tDX2 Setup was found on this system"
	if [ "$DX2VERSION" < "$__DXVERSION__" ]; then
		echo -en "The currently installed version ("$DX2VERSION") is older.\n\nWould you like to update?: "
	else
		echo -en "The currently installed version ("$DX2VERSION") is current and up to date. \n\n"
	fi
else
	echo -en "\r \033[00;01m[\033[00;01;38;5;196m✗\033[00;01m]\n\tDX2 Setup was not found on this system\n\n[ HIT ANY KEY TO CONTINUE ]\n\n"
	read
	__DXTITLE "CHECKING FOR DX2 DIRS: "
	echo -en "\033[00;01m[\033[38;5;196m-\033[00;01m] LOADING VARIABLES\033[m\n"
	echo -en """ \033[00;01m[\033[38;5;190m⏳\033[00;01m]   Loading VARs..."""
	sleep .4
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
	echo -en "\r \033[00;01m[\033[00;01;38;5;46m✔\033[00;01m]\033[00;01m\n\n\033[00;01m[\033[38;5;196m-\033[00;01m] CHECKING FOR DIRECTORIES\033[m\n"
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

	unset -f __check_dir
##
### FUNCTION - __check_dx2rc() ###
#__DXTITLE "CHECKING FOR DX2RC: "
#function __check_dx2rc(){
	echo -en """\n[-] Checking for DX2 Startup file:
 \033[00;01m[\033[38;5;190m⏳\033[00;01m]  Locating file"""
 	sleep .4
 	if [ ! -f ~/.dx2rc ]; then
		echo -en """\r \033[00;01m[\033[00;01;38;5;196m✗\033[00;01m]\n\tCreating file: \t\033[m"""
		sleep .4
		echo -en """## Load VARs
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

export CDPATH=~/.Shortcuts""" > ~/.dx2rc;
		echo -en "\033[00;01m[\033[00;01;32mDONE\033[00;01m]\n\n"
	else
		echo -en "\r \033[00;01m[\033[00;01;38;5;46m✔\033[00;01m]\033[00m\n\n\n"
	fi
#}


##
# STEP4 - EDIT BASHRC OR ZSHRC
#__DXTITLE "MODIFY RC FILE TO LOAD DX2RC"
echo -en """
[-] \033[00;01mChecking for .bashrc:\033[m """
sleep .5
if [ -f ~/.bashrc ]; then
	echo -en "\033[00;01m[\033[00;01;32m FOUND\033[00;01m ]\n\t\033[00;01mChecking for modifications:\033[m "
	sleep .5
	if [ "$(cat ~/.bashrc | grep -qe 'source ~/.dx2rc'; echo $?)" != 0 ]; then
		echo -en "\033[00;01m[\033[00;01;31m NOT FOUND\033[00;01m ]\n\t\033[00;01mEditing .bashrc file now ...:\033[m "
		sleep .5
		echo -en """### BEG - LOAD DX2RC ###
if [ -f ~/.dx2rc ]; then
	source ~/.dx2rc;
fi
### END - LOAD DX2RC ###
""" >> ~/.bashrc
		echo -en "\033[00;01m[ \033[00;01;32mDONE\033[00;01m ]\033[m\n\n"
	else
		echo -en "\033[00;01m[\033[00;01;32m FOUND\033[00;01m ]\033[m\n\n"
	fi
fi

echo -en "\033[00;01mChecking for .zshrc:\033[m "
sleep .5
if [ -f ~/.zshrc ]; then
	echo -en "\033[00;01m[\033[m \033[00;01;32mFOUND\033[m \033[00;01m]\033[m\n\t\033[00;01mChecking for modifications:\033[m "
	sleep .5
	if [ "$(cat ~/.zshrc | grep -qe 'source ~/.dx2rc'; echo $?)" != 0 ]; then
		echo -en "\033[00;01m[\033[00;01;31m NOT FOUND\033[00;01m ]\n\tEditing .zshrc file now ...:\033[m "
		sleep .5
		echo -en """### BEG - LOAD DX2RC ###
if [ -f ~/.dx2rc ]; then
	source ~/.dx2rc;
fi
### END - LOAD DX2RC ###""" >> ~/.zshrc
		echo -en "\033[00;01m[\033[00;01;32m DONE \033[00;01m]\033[m\n\n"
	else
		echo -en "\033[00;01m[\033[00;01;32m FOUND\033[00;01m ]\033[m\n\n"
	fi
fi

fi

