#!/bin/zsh

for filename in `ls configs` 
do
    echo "----------------------------------------------------"
    echo "$filename"
    ./pcalc.py configs/$filename
done

