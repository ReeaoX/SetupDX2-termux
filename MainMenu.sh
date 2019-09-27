#!/bin/bash

__DXVERSION__='2.1'

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
	if [ $DX2VERSION ]; then
		echo -en "\033[00;03mDX2 Setup v"$DX2VERSION" was found \033[01;32minstalled\033[00;03m on this system.\033[m\n"
	else
		echo -en "\033[00;03mDX2 Setup is \033[01;31mnot installed\033[00;03m on this system.\033[m\n"
	fi
	echo -en """
	\033[00;;01;38;5;46m[\033[00;01m1\033[00;;01;38;5;46m]\033[00;01m	(Re)Install / Update DX2Setup
	\033[00;;01;38;5;46m[\033[00;01m2\033[00;;01;38;5;46m]\033[00;01m	Install Addons
	\033[00;;01;38;5;46m[\033[00;01m3\033[00;;01;38;5;46m]\033[00;01m	Check for updates

	\033[00;;01;38;5;190m[\033[00;01mH\033[00;;01;38;5;190m]\033[00;01m	Help
	\033[00;;01;38;5;196m[\033[00;01mX\033[00;;01;38;5;196m]\033[00;01m	Exit

 : """
 	read -n 1 -r MAINMENUOPT

}

__dx2_mainmenu