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


2. How many countries are there and how would you count?


3. How many graphs did you make? If the number is different than above, how could you investigate?

## Hints and solutions
To see a version of this repository with the necessary scripts outlined for you, checkout the `with_clues` branch. For one with solutions, checkout `solutions`.
