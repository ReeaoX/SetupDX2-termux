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
#☐☑☒

#⧖⌛
