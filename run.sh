#!/bin/bash

SLEEP=0.2

cd $(dirname $0)

run_chapter(){
    [ ! -e $1 ] && echo "No directory [$1]" && exit -1

    ## Go into a chapter directory
    pushd $1
    [ -e env.sh ] && source env.sh
    [ ! -e outputs ] && mkdir -v outputs

    ## Loop over each file (*.py, *.sh, *.sql)
    for p in $(ls section*_[0-9]?_*.py section*_[0-9]??_*.py section*_[0-9]?_*.sh section*_[0-9]?_*.sql)
    do
	local basename="${p%%.*}"
	case "${p#*.}" in
	     py)
		 run_python $p $basename &
		 sleep $SLEEP
		 ;;
	     sh)
		 run_bash $p $basename &
		 sleep $SLEEP
		 ;;
	     sql)
		 [ -z "$DATABASE" ] && echo "No Database" && continue
		 run_sql $p $basename &
		 sleep $SLEEP
		 ;;
	     *)
		 echo "Not supported [$p]"
		 ;;
	esac
    done
    popd
}

check_output(){
    local p=$1
    local basename=$2
    local return=$3

    case $return in
	0) echo "[$p] ==> OK"
	   [ -s outputs/${basename}.txt ] || rm -v outputs/${basename}.txt
	   ;;
	*) echo "[$p] ==> Error [$?]"
	   cat outputs/${basename}.txt
	   ;;
    esac
}

run_python(){
    local p=$1
    local basename=$2
    python3 $p > outputs/${basename}.txt
    check_output $p $basename $?
}

run_bash(){
    local p=$1
    local basename=$2
    bash $p &> outputs/${basename}.txt
    check_output $p $basename $?
}

run_sql(){
    local p=$1
    local basename=$2
    [ -e "width.sqlite" ] && WIDTH=width.sqlite
    cat $WIDTH $p | sqlite3 -column -header ${DATABASE}.db &> outputs/${basename}.txt
    check_output $p $basename $?
}


[ $# -eq 0 ] && echo "$0 [chapterX]" && exit 0
run_chapter $1
