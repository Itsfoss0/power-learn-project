#!/usr/bin/env bash
#print natural numbers from 1 - 50
#one way to do it
#for (( num=0; num<=50; num++)); do
#    echo "$num";
#done;

for number in {1..50}; do
    echo -e "$number";
done;
