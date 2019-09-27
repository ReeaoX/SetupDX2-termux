#!/bin/bash

__DXVERSION__='0.1'

clear
Title="DX2 Setup v"$__DXVERSION__""

function __drawtitlebar(){
	clear
	printf '\033[00;01;41;38;5;15m'
	printf ' %.s' $(seq 1 $COLUMNS)
	printf "\r $Title\033[m\n\n"
}

function __dx2_mainmenu(){
	__drawtitlebar
	echo -en """
	[1]	Check
	[2]	Setup
	[3]	Addons

: """
}

__dx2_mainmenu