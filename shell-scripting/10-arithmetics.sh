#!/usr/bin/env bash
# evaluate mathematical expressions

echo -n "Enter a valid expression: ";
read -r expression

printf "%.3f \n" $(echo "$expression" | bc -l);
