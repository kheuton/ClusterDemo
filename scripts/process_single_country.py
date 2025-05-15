import argparse
import os
import pandas as pd
from graphing_utils import plot_values


def main(iso2, country_name, data_root_dir):
    # Construct the file path
    file_path = # TODO
    
    data = pd.read_csv(file_path)

    
    # Plot the data
    output_dir = os.path.join(data_root_dir, iso2)
    #TODO call plot_values


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process data for a single country.")
    parser.add_argument(#TODO add arguments))
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    main()#TODO add arguments)

