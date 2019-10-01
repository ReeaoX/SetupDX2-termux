__DXVERSION__=2.4

### CHECK FOR DX2 ###
__DXTITLE "DX2 Setup"
echo -en "\033[00;01m[\033[38;5;196m-\033[00;01m] CHECKING SYSTEM FOR DX2 SETUP\033[m\n"
echo -en """ \033[00;01m[\033[38;5;190m🔍 \033[00;01m]  \033[00;01mSearching system\033[00;01m "
if [ $DX2VERSION ]; then
	echo -en "\r \033[00;01m[\033[00;01;38;5;46m✔\033[00;01m] \033[00m\n\tDX2 Setup was found on this system\n\t"
	if [ "$DX2VERSION" > "$__DXVERSION__" ]; then
		echo -en "The currently installed version ("$DX2VERSION") is older.\n\nWould you like to update?: "
	else
		echo -en "The currently installed version ("$DX2VERSION") is current and up to date. \n\n"
	fi
else
	echo -en "\r \033[00;01m[\033[00;01;38;5;196m✗\033[00;01m]\n\tDX2 Setup was not found on this system\n\n[ HIT ANY KEY TO CONTINUE ]\n\n"
	read
fi
