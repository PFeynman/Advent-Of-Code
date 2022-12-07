#!/bin/bash

filename='input.txt'
sums=()
current_sum=0
while read line; do
	if [ -z "$line" ]; then
		sums+=($current_sum)
		current_sum=0
	else
		current_sum=$(($current_sum+$line))
	fi
done < $filename

IFS=$'\n'
echo "${sums[*]}" | sort -nr | head -n3 | awk '{ sum += $1 } END { print sum}'
