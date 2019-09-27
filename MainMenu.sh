#!/bin/bash

__DXVERSION__='0.1'

clear
Title="DX2 Setup v"$__DXVERSION__""

function __drawtitlebar(){
	clear
	printf '\033[00;01;41;38;5;15m'
	printf ' %.s' $(seq 1 $COLUMNS)
	printf "\r $Title\033[m\n"
}

function __dx2_mainmenu(){
	__drawtitlebar
	if [ $DX2 ] && [ -d "$HOME"/.DX2 ] && [ -f "$HOME"/.dx2rc ]; then
		echo -en "\033[00;03mDX2 Setup appears to be \033[32mcorrectly\033[00;03m installed on this system.\033[m\n"
	else
		echo -en "\033[00;03mDX2 Setup \033[31mdoesn't\033[00;03m appear to be correctly installed on this system.\033[m\n"
	fi
	echo -en """
	[1]	Check
	[2]	Setup
	[3]	Addons

: """
}

__dx2_mainmenu