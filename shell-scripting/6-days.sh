#!/usr/bin/env bash
#Determine which day it is

day=$(date +"%u");
seson=$(date +"%p");

if [[ $day -lt 5 ]]; then
    echo  -n "Its a weekday mate";
    if [[ $seson == "PM" ]]; then
	echo "  afternoon";
    else
	echo "  morning";
    fi
else
    echo "Its the weekend: $(date +"%a")";
fi
