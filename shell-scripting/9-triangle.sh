#!/usr/bin/env bash
# determine the type of a triangle

echo  -n "Enter the dimensions of side 1: ";
read -r side_1;
echo -n "Enter the dimensions of side 2: ";
read -r side_2;
echo -n "Enter the dimensions of side 3: ";
read -r side_3

if [[ "$side_1" -eq "$side_2" && "$side_2" -eq "$side_3" ]]; then
    echo "EQUILATERAL";

elif [[ "$side_1" -eq "$side_2" || "$side_1" -eq "$side_3" || "$side_2" -eq "$side_3" ]]; then
    echo "ISOSCELES";
else
    echo "SCALENE";
fi