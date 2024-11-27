import re

def clean_pu_column_with_misc(dataframe, column_name):
    print(f"\nProcessing column: {column_name}")
    
    # Define regex for valid PU# format (6 alphanumeric characters)
    valid_pu_regex = re.compile(r"^[A-Za-z0-9]{6}$")

    # Step 1: Identify valid and invalid entries
    valid_pu = dataframe[column_name].astype(str).str.match(valid_pu_regex, na=False)

    # Step 2: Create PU# MISC column for invalid entries
    pu_misc_column = dataframe[column_name][~valid_pu]
    
    # Step 3: Keep valid entries in PU# column and uppercase them
    dataframe[column_name] = dataframe[column_name][valid_pu].str.upper()
    
    # Step 4: Fill missing values in both columns
    dataframe[column_name] = dataframe[column_name].fillna("")
    pu_misc_column = pu_misc_column.fillna("")
    
    # Step 5: Insert PU# MISC column next to PU#
    pu_column_index = dataframe.columns.get_loc(column_name)
    dataframe.insert(pu_column_index + 1, "PU# MISC", pu_misc_column)
    
    # Debugging output
    print(f"\nValid PU# entries in {column_name}:")
    print(dataframe[column_name].unique())
    print(f"\nInvalid PU# entries moved to PU# MISC:")
    print(dataframe["PU# MISC"].unique())

    return dataframe
