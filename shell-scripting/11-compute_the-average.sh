#!/usr/bin/env bash
# compute the average of `N` integers
# to 3 decimal places

total=0;
echo -n  "How many integer values? ";
read -r times;
times_tmp=$times
while [ "$times" -gt 0 ]; do
    echo -n "Enter number ($times): ";
    read -r num;
    total=$((total+num))
    times=$((times-1));
done
average=$((total/times_tmp));
echo "The average is $average";
