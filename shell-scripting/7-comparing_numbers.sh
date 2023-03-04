#!/usr/bin/env bash
# Comparing numbers

echo -n "Enter the first number: ";
read -r number_1;
echo -n "Enter the second number: ";
read -r number_2;

if [ "$number_1" -gt "$number_2" ]; then
    echo "$number_1 is greater than $number_2";
elif [ "$number_1" -lt "$number_2" ]; then
    echo "$number_1 is less than $number_2";
else
    echo "$number_1 is equal to $number_2";
fi
