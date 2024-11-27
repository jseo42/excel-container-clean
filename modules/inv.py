def clean_inv_status_column(dataframe, column_name):
   
    print(f"\nProcessing column: {column_name}")
    print(f"Available columns: {dataframe.columns.tolist()}")  # Debug column names
    
    # Step 1: Extract numbers or text after 'done' (case-insensitive) or '#'
    inv_number_column = dataframe[column_name].str.extract(r'[Dd]one(?:.*?[#\s]*)(.*)', expand=False)
    print("\nExtracted Inv Number:")
    print(inv_number_column.head())  # Debug extracted numbers
    
    # Step 2: Standardize 'done' variations to "DONE" in Inv status
    dataframe[column_name] = dataframe[column_name].str.contains(r'[Dd]one', na=False).replace({True: "DONE", False: ""})
    print("\nUpdated Inv status column:")
    print(dataframe[column_name].unique())  # Debug updated column
    
    # Step 3: Remove '#' from Inv Number column and handle empty values
    inv_number_column = inv_number_column.str.replace("#", "", regex=False).str.strip()
    
    # Step 4: Fill missing values in both columns
    dataframe[column_name] = dataframe[column_name].fillna("")
    inv_number_column = inv_number_column.fillna("")  # Keep empty if there's no value
    
    # Step 5: Insert 'Inv Number' column next to 'Inv status'
    status_column_index = dataframe.columns.get_loc(column_name)
    dataframe.insert(status_column_index + 1, "Inv Number", inv_number_column)
    
    # Debugging output
    print(f"\nGenerated Inv Number column:")
    print(dataframe["Inv Number"].unique())
    
    return dataframe
