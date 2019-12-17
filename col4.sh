#! /bin/bash


for i in $(seq 1 1 20)
do
python variation.py   $i 1 1 0.1
python variation.py  $i 0 1 0.1
python variation.py  $i 1 0 0.1
done

