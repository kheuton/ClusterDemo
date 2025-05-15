#!/usr/bin/env bash
#SBATCH --job-name=process_country
#SBATCH --output=process_country_%j.out
#SBATCH --error=process_country_%j.err
#SBATCH --time=01:00:00
#SBATCH --partition=batch
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G

# Run the script with provided arguments
python ./scripts/process_single_country.py "$@"