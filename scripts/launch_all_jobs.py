import csv
import subprocess
import os

# Path to the countries CSV file
countries_file = './data/countries.csv'

# Path to the SLURM script
slurm_script = './scripts/run_job.slurm'

# Path to the data directory
data_dir = os.path.abspath('./data')

# Read countries from the CSV file
with open(countries_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        country_name = row['country']
        iso2 = row['iso2']

        # Construct the sbatch command with flags
        command = # TODO: Construct the sbatch command

        # Submit the job
        subprocess.run(command)