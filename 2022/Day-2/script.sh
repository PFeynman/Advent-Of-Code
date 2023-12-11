#!/bin/bash

filename='input.txt'

declare -A rps=( [A]=0 [B]=1 [C]=2 [X]=0 [Y]=1 [Z]=2 )
declare -A choice_points=( [X]=1 [Y]=2 [Z]=3)
points=0

while read line; do
    p1=${rps[${line:0:1}]}
    p2=${rps[${line:2:1}]}

    if [ "$p1" -eq "$p2" ]; then
        points=$(( $points + 3 ))
    elif [ $(( $p1 + 1 % 3 )) -eq "$p2" ]; then
        points=$(( $points + 6 ))
    fi

    points=$(( $points + ${choice_points[${line:2:1}]} ))
done < $filename

echo $points