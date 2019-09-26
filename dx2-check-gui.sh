#!/bin/bash

CHECKY="\033[00;01m❲\033[00;01;38;5;46m✔\033[00;01m❳\033[m"
CHECKN="\033[00;01m❲\033[00;01;38;5;196m✗\033[00;01m❳\033[m"
CHECKW="\033[00;01m❲\033[00;01;38;5;190m⧖❳\033[m"

function __check_var(){
sleep .1;
if [ $DX2 ]; then
	echo -en "$CHECKY"
	tput cud 1
	printf '\r'
else
	echo -en "$CHECKN"
	SETUPREQ=1
	tput cud 1
	printf '\r'
fi
sleep .1;
if [ $DX2BIN ]; then
	echo -en "$CHECKY"
	tput cud 1
	printf '\r'
else
	echo -en "$CHECKN"
	SETUPREQ=1
	tput cud 1
	printf '\r'
fi
sleep .1;
if [ $DX2DATA ]; then
	echo -en "$CHECKY"
	tput cud 1
	printf '\r'
else
	echo -en "$CHECKN"
	SETUPREQ=1
	tput cud 1
	printf '\r'
fi
sleep .1;
if [ $DX2RC ]; then
	echo -en "$CHECKY"
	tput cud 1
	printf '\r'
else
	echo -en "$CHECKN"
	SETUPREQ=1
	tput cud 1
	printf '\r'
fi
sleep .1;
if [ $DX2BAK ]; then
	echo -en "$CHECKY"
	tput cud 1
	printf '\r'
else
	echo -en "$CHECKN"
	SETUPREQ=1
	tput cud 1
	printf '\r'
fi
sleep .1;
if [ $DX2TMP ]; then
	echo -en "$CHECKY"
	tput cud 1
	printf '\r'
else
	echo -en "$CHECKN"
	SETUPREQ=1
	tput cud 1
	printf '\r'
fi
sleep .1;
if [ $DX2GIT ]; then
	echo -en "$CHECKY"
	tput cud 1
	printf '\r'
else
	echo -en "$CHECKN"
	SETUPREQ=1
	tput cud 1
	printf '\r'
fi
sleep .1;
if [ $DX2FUNCS ]; then
	echo -en "$CHECKY"
	tput cud 1
	printf '\r'
else
	echo -en "$CHECKN"
	SETUPREQ=1
	tput cud 1
	printf '\r'
fi
sleep .1;
if [ $DX2ALIASES ]; then
	echo -en "$CHECKY"
	tput cud 1
	printf '\r'
else
	echo -en "$CHECKN"
	SETUPREQ=1
	tput cud 1
	printf '\r'
fi
sleep .1;
if [ $DX2SHORTCUTS ]; then
	echo -en "$CHECKY"
	tput cud 3
	printf '\r'
else
	echo -en "$CHECKN"
	SETUPREQ=1
	tput cud 3
	printf '\r'
fi
}

function __check_dir(){
	__load_vars
	sleep .1;
	if [ -d $DX2 ]; then
		echo -en "$CHECKY"
		tput cud 1
		printf '\r'
	else
		echo -en "$CHECKN"
		SETUPREQ=1
		tput cud 1
		printf '\r'
	fi
	sleep .1;
	if [ -d $DX2BIN ]; then
		echo -en "$CHECKY"
		tput cud 1
		printf '\r'
	else
		echo -en "$CHECKN"
		SETUPREQ=1
		tput cud 1
		printf '\r'
	fi
	sleep .1;
	if [ -d $DX2DATA ]; then
		echo -en "$CHECKY"
		tput cud 1
		printf '\r'
	else
		echo -en "$CHECKN"
		SETUPREQ=1
		tput cud 1
		printf '\r'
	fi
	sleep .1;
	if [ -d $DX2RC ]; then
		echo -en "$CHECKY"
		tput cud 1
		printf '\r'
	else
		echo -en "$CHECKN"
		SETUPREQ=1
		tput cud 1
		printf '\r'
	fi
	sleep .1;
	if [ -d $DX2BAK ]; then
		echo -en "$CHECKY"
		tput cud 1
		printf '\r'
	else
		echo -en "$CHECKN"
		SETUPREQ=1
		tput cud 1
		printf '\r'
	fi
	sleep .1;
	if [ -d $DX2TMP ]; then
		echo -en "$CHECKY"
		tput cud 1
		printf '\r'
	else
		echo -en "$CHECKN"
		SETUPREQ=1
		tput cud 1
		printf '\r'
	fi
	sleep .1;
	if [ -d $DX2GIT ]; then
		echo -en "$CHECKY"
		tput cud 1
		printf '\r'
	else
		echo -en "$CHECKN"
		SETUPREQ=1
		tput cud 1
		printf '\r'
	fi
	sleep .1;
	if [ -d $DX2FUNCS ]; then
		echo -en "$CHECKY"
		tput cud 1
		printf '\r'
	else
		echo -en "$CHECKN"
		SETUPREQ=1
		tput cud 1
		printf '\r'
	fi
	sleep .1;
	if [ -d $DX2ALIASES ]; then
		echo -en "$CHECKY"
		tput cud 1
		printf '\r'
	else
		echo -en "$CHECKN"
		SETUPREQ=1
		tput cud 1
		printf '\r'
	fi
	sleep .1;
	if [ -d $DX2SHORTCUTS ]; then
		echo -en "$CHECKY"
		tput cud 3
		printf '\r'
	else
		echo -en "$CHECKN"
		SETUPREQ=1
		tput cud 3
		printf '\r'
	fi
}

function __load_vars(){
	export DX2="$HOME/.DX2"
	export DX2BIN="$DX2/bin"
	export DX2FILES="$DX2/files"
	export DX2RC="$DX2/rc"
	export DX2BAK="$DX2/backups"
	export DX2TMP="$DX2/temp"
	export DX2GIT="$DX2/git"
	export DX2FUNCS="$DX2/functions"
	export DX2ALIASES="$DX2/aliases"
}

function __check_dx2rc(){
	sleep .1;
	if [ -f $HOME/.dx2rc ]; then
		echo -en "$CHECKY"
		tput cud 3
		printf '\r'
	else
		echo -en "$CHECKN"
		SETUPREQ=1
		tput cud 3
		printf '\r'
	fi
}


function __check_editedrc(){
	sleep .1;
	if [ ! -f $HOME/.bashrc ]; then
		echo -en "$CHECKY"
		tput cud 1
		printf '\r'
	else
		if [ "$(cat ~/.bashrc | grep -qe 'source ~/.dx2rc'; echo $?)" -eq 0 ]; then
			echo -en "$CHECKY"
			tput cud 1
			printf '\r'
		else
			echo -en "$CHECKN"
			SETUPREQ=1
			tput cud 1
			printf '\r'
		fi
	fi
	sleep .1;
	if [ ! -f $HOME/.zshrc ]; then
		echo -en "$CHECKY"
		tput cud 1
		printf '\r'
	else
		if [ "$(cat ~/.zshrc | grep -qe 'source ~/.dx2rc'; echo $?)" -eq 0 ]; then
			echo -en "$CHECKY"
			tput cud 1
			printf '\r'
		else
			echo -en "$CHECKN"
			SETUPREQ=1
			tput cud 1
			printf '\r'
		fi
	fi
}
if [ "$SETUPREQ" -eq 1 ]; then
	echo -en """
One or more elements is missing.

You will need to run the dx2setup script.

[ HIT ANY KEY TO CONTINUE ]

"""
	read
else
	echo -en """
All of the dx2 elements were found.

No futher setup is required.

[ HIT ANY KEY TO CONTINUE ]

"""
	read
fi
}

#THINGS TO CHECK FOR
function __runcheck(){
	SETUPREQ=0
	clear;
	echo -en """
\033[1;4mCheck if vars are loaded:\033[m
""";
	tput sc;
	echo -en """"$CHECKW" \$DX2
"$CHECKW" \$DX2BIN
"$CHECKW" \$DX2DATA
"$CHECKW" \$DX2RC
"$CHECKW" \$DX2BAK
"$CHECKW" \$DX2TMP
"$CHECKW" \$DX2GIT
"$CHECKW" \$DX2FUNCS
"$CHECKW" \$DX2ALIASES
"$CHECKW" \$DX2SHORTCUTS

\033[1;4mCheck if DIR exists:\033[m
"$CHECKW" \$DX2
"$CHECKW" \$DX2BIN
"$CHECKW" \$DX2DATA
"$CHECKW" \$DX2RC
"$CHECKW" \$DX2BAK
"$CHECKW" \$DX2TMP
"$CHECKW" \$DX2GIT
"$CHECKW" \$DX2FUNCS
"$CHECKW" \$DX2ALIASES
"$CHECKW" \$DX2SHORTCUTS

\033[1;4mCheck if file(s) exists:\033[m
"$CHECKW" \$HOME/.dx2rc

\033[1;4mCheck if rc file(s) are edited:\033[m
"$CHECKW" Edited ~/.bashrc
"$CHECKW" Edited ~/.zshrc

""";
	tput rc;
	__check_var;
	__check_dir;
	__check_dx2rc;
	__check_editedrc
}

__runcheck