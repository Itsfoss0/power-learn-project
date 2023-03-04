#!/usr/bin/env bash
# Yes or no

read  -r string;

if [[ -n "$string" ]]; then
    case $string in
	y | Y)
	    echo "YES";;
	n| N)
	    echo "NO";;
	*)
	    echo "No";;
    esac
else
    echo "Not part of the plan"
fi

