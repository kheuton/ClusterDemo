import argparse
import os
import pandas as pd
from graphing_utils import plot_values


def main(iso2, country_name, data_root_dir):
    # Construct the file path
    file_path = os.path.join(data_root_dir, iso2, "imports.csv")
    
    # Read the data
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: File at {file_path} is empty")
        return
    
    # Ensure the required columns exist
    if 'value' not in data.columns:
        print(f"Error: 'value' column not found in {file_path}")
        return
    
    # Plot the data
    output_dir = os.path.join(data_root_dir, iso2)
    plot_values(data, country_name, output_dir)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process data for a single country.")
    parser.add_argument('--iso2', required=True, help="ISO2 code of the country (e.g., 'US').")
    parser.add_argument('--country_name', required=True, help="Name of the country (e.g., 'United States').")
    parser.add_argument('--data_root_dir', required=True, help="Root directory of the data.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    print(f"ISO2: {args.iso2}")
    print(f"Country Name: {args.country_name}")
    print(f"Data Root Directory: {args.data_root_dir}")
    main(args.iso2, args.country_name, args.data_root_dir)

