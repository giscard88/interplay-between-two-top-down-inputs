#! /bin/bash


for i in $(seq 1 1 20)
do
python experiment_lfp.py  $i 1 1
python experiment_lfp.py  $i 0 1
python experiment_lfp.py  $i 1 0
done



