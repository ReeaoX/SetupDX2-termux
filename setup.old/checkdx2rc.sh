### FUNCTION - __check_dx2rc() ###
__DXTITLE "CHECKING FOR DX2RC: "
#function __check_dx2rc(){
	echo -en """Checking for DX2 Startup file:
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

