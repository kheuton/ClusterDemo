import os

import matplotlib.pyplot as plt

def plot_values(dataframe, country_name, output_directory):
    """
    Given a dataframe with 'year' and 'value' columns, a country name, and an output directory,
    this function creates a line plot of the values over the years and saves the plot as a PNG file
    in the specified output directory.

    Parameters:
        dataframe (pd.DataFrame): A pandas DataFrame containing 'year' and 'value' columns.
        country_name (str): The name of the country to include in the plot title and filename.
        output_directory (str): The directory where the plot PNG file will be saved.

    Returns:
        None
    """
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(dataframe['year'], dataframe['value'], marker='o', linestyle='-', color='b')
    plt.title(f'{country_name} - Values Over Years', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Value', fontsize=14)
    plt.grid(True)
    plt.tight_layout()

    # Save the plot as a PNG file
    output_file = os.path.join(output_directory, f"{country_name}_values_plot.png")
    plt.savefig(output_file)
    plt.close()