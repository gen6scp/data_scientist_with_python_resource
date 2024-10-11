## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section2_01_dictionary_to_dataframe_1 import city_df

sys.stdout = org_stdout


# Define custom row labels
city_labels = ['NYC', 'LA', 'CHI', 'HOU', 'PHX']

# Assign these labels to the DataFrame index
city_df.index = city_labels

# Print the updated DataFrame
print(city_df)
