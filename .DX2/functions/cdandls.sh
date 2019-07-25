function cdandls(){
	if [ ! $1 ]; then
		\cd;
	else
		CDDIR=$1
		builtin cd "$CDDIR"
		la;
		unset CDDIR
	fi
}

alias cd=cdandls