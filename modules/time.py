import re

def clean_time_column_with_misc(dataframe, column_name):
    print(f"\nProcessing column: {column_name}")
    
    # Define regex for valid time format (HH:MM:SS)
    valid_time_regex = re.compile(r"^\d{2}:\d{2}:\d{2}$")

    # Step 1: Identify valid and invalid entries
    valid_times = dataframe[column_name].astype(str).str.match(valid_time_regex, na=False)

    # Step 2: Create TIME MISC column for invalid entries
    time_misc_column = dataframe[column_name][~valid_times]
    
    # Step 3: Keep valid times in the TIME column
    dataframe[column_name] = dataframe[column_name][valid_times]
    
    # Step 4: Fill missing values in both columns
    dataframe[column_name] = dataframe[column_name].fillna("")
    time_misc_column = time_misc_column.fillna("")
    
    # Step 5: Insert TIME MISC column next to TIME
    time_column_index = dataframe.columns.get_loc(column_name)
    dataframe.insert(time_column_index + 1, "TIME MISC", time_misc_column)
    
    # Debug output for validation
    print(f"\nValid TIME entries in {column_name}:")
    print(dataframe[column_name].unique())
    print(f"\nInvalid TIME entries moved to TIME MISC:")
    print(dataframe['TIME MISC'].unique())

    return dataframe
