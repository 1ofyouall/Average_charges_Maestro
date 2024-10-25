#It is necessary to specify the resulting weight coefficients for each conformation file, 
#as well as indicate the correct line numbers containing the geometry and charges of the structure.

import pandas as pd
import os

# Path to the directory with .mol2 files obtained after conformational search and charges calculation in Maestro
directory = 'your_path'

# Set your weighting factors
# The weight coefficients are obtained during the molecular conformational search 
# and correspond to the probability of obtaining a certain conformation.
weight_coefficients = [30, 20, 15, 10, 5, 3, 2, 1]  # for example
weighted_sum = None

# Get a list of all files with the .mol2 extension and sort them by name
files = sorted([f for f in os.listdir(directory) if f.endswith('.mol2')], key=lambda x: int(os.path.splitext(x)[0]))

for i, filename in enumerate(files):
    file_path = os.path.join(directory, filename)

    # Reading a file    
    with open(file_path, 'r') as f:
        # Required lines (in this case 8-460 inclusive) depending on molecule!!!
        lines = f.readlines()[8:461]
        
        # Converting strings to a list
        data = [line.strip().split() for line in lines]
        
        # Create a DataFrame and specify column names
        df = pd.DataFrame(data, columns=['column1', 'atom', 'column3', 'column4', 'column5', 'column6', 'column7', 'column8', 'charge'])

        # Convert the data in the last column 'charge' to float numbers
        df['charge'] = df['charge'].astype(float)
        #print(df['charge'])
        
        # Get the weighting factor for the current file
        weight = weight_coefficients[i]

        # Multiply the last column 'charge' by the weighting factor
        df['weighted_charge'] = df['charge'] * weight
        #print(df[['charge', 'weighted_charge']])

        # Summarize the weighted data
        if weighted_sum is None:
            weighted_sum = df['weighted_charge']
        else:
            weighted_sum += df['weighted_charge']

# New average data in csv table
average_data = weighted_sum / sum(weight_coefficients)
print(average_data)
average_data.to_csv('new_charges.csv')

