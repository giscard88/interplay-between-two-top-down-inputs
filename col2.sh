#! /bin/bash

for i in $(seq 1 1 20)
do
for j in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
do
python variation.py  $i 1 1 $j

done
done
