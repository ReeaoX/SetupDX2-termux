# STEP4 - EDIT BASHRC OR ZSHRC
__DXTITLE "MODIFY RC FILE TO LOAD DX2RC"
echo -en """
\033[00;01mChecking for .bashrc:\033[m """
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
