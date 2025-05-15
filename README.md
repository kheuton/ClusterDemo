# ClusterDemo
Demo of Tufts HPC

## Challenges

This repo is here to help you learn to use the Tufts HPC by writing your own distributed jobs.

The data folder contains the following
    - A file called `countries.csv` which contains every country's name and its iso2 code
    - A folder named with every iso2 code
    - Inside each folder is a file called `imports.csv` that contains data on a countries imports

The goal is to create a graph of every country's import data, and save it in the same folder containing that countries data. You could trivially do this with a for-loop, but what if you wanted to do some processing that took hours? You need to create the scripts necessary to launch these jobs and make these graphs.

There is a graphing function in scripts/graphing_utils.py that you can use.

## Questions

1. What files do you need to create?
    > A python script that will graph a single country

    > A slurm file that will call that script for a single country
    
    > A file that loops over all countries and submits the slurm script.

1. How many countries are there and how would you count?
    > 248

    > `ls -lth data | wc -l` = 250, subtract 2: 1 for the header and 1 for the countries.csv

    > `cat data/countries.csv | wc -l` = 249, subtract 1 for the header

2. How many graphs did you make? If the number is different than above, how could you investigate?
    > 247

    > `grep Error .*`, this function searches every file for the text 'Error'
    
    > The error is in a .out file (and not a .err) because the error was handled by the script and not raised. 