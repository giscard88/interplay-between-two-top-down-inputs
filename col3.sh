#! /bin/bash


for i in $(seq 1 1 20)
do
python variation.py   $i 1 1 0.8
python variation.py  $i 0 1 0.8
python variation.py  $i 1 0 0.8
done


for i in $(seq 1 1 20)
do
python variation.py   $i 1 1 1.0
python variation.py  $i 0 1 1.0
python variation.py  $i 1 0 1.0
done


for i in $(seq 1 1 20)
do
python variation.py   $i 1 1 0.6
python variation.py  $i 0 1 0.6
python variation.py  $i 1 0 0.6
done

for i in $(seq 1 1 20)
do
python variation.py   $i 1 1 0.4
python variation.py  $i 0 1 0.4
python variation.py  $i 1 0 0.4
done





