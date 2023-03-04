#!/usr/bin/env bash
# world of numbers

echo -n "Enter first number: ";
read -r num_a
echo -n "Enter second number: ";
read -r num_b

echo "$((num_a + num_b))";
echo "$((num_a - num_b))";
echo "$((num_a * num_b))";
echo "$((num_a / num_b))";

