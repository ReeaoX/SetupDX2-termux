#!/bin/bash

CHECKY="\033[00;01m❲\033[00;01;38;5;46m✔\033[00;01m❳\033[m"
CHECKN="\033[00;01m❲\033[00;01;38;5;196m✗\033[00;01m❳✔\033[m"
CHECKW="\033[00;01m❲\033[00;01;38;5;190m⧖❳\033[m"

#THINGS TO CHECK FOR
clear;
echo -en """
\033[1mCheck if vars are loaded:\033[m
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

\033[1mCheck if file(s) exists:\033[m
"$CHECKW" \$HOME/.dx2rc

\033[1mCheck if rc file(s) are edited:\033[m
"$CHECKW" Edited ~/.bashrc
"$CHECKW" Edited ~/.zshrc

""";
tput rc;
sleep 1;
if [ $DX2 ]; then
	echo -en "$CHECKY"
	tput cud 1
	printf '\r'
else
	echo -en "$CHECKN"
	tput cud 1
	printf '\r'
fi
sleep 1;
if [ $DX2BIN ]; then
	echo -en "$CHECKY"
	tput cud 1
	printf '\r'
else
	echo -en "$CHECKN"
	tput cud 1
	printf '\r'
fi
tput cud 16;