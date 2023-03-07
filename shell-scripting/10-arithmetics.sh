#!/usr/bin/env bash
# evaluate mathematical expressions

echo -n "Enter a valid expression: ";
read -r expression

echo "$expression" | bc -l;
