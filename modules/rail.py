# Define the mapping dictionary
RAIL_MAPPING = {
    "BNSF": "BNSF",
    "BNSF - Alliance" : "BNSF Alliance",
    "BNSF DALLAS RAIL": "BNSF DALLAS",
    "BNSF - Kansas City LPKC" : "BNSF Kansas City LPKC",
    "BNSF LPC?": "BNSF LPC",
    "NS -- APPLIANCE PARK ?": "NS APPLIANCE PARK",
    "UP G4": "UP GLOBAL 4",
    "NA": "UNKNOWN",
    "SAVANNAH GARDEN CITY TERMINAL L738": "SAVANNAH GARDEN CITY TERMINAL",
    "MAHER TERMINALS": "MAHER TERMINAL",
    # Add more entries as needed
}

def clean_rail_column(dataframe, column_name):
    """
    Cleans and standardizes the Rail column using a mapping dictionary.
    Converts all entries to uppercase before applying the mapping.
    
    Args:
        dataframe (pd.DataFrame): The DataFrame containing the Rail column.
        column_name (str): The name of the Rail column to process.
    
    Returns:
        pd.DataFrame: The updated DataFrame with cleaned Rail column.
    """
    print(f"\nProcessing column: {column_name}")
    
    # Convert all entries to uppercase
    dataframe[column_name] = dataframe[column_name].str.upper().str.strip()
    
    # Apply the mapping
    dataframe[column_name] = dataframe[column_name].replace(RAIL_MAPPING)
    
    # Handle missing or unknown values
    dataframe[column_name] = dataframe[column_name].fillna("UNKNOWN")
    
    # Debugging output
    print("\nUpdated Rail column:")
    print(dataframe[column_name].unique())
    
    return dataframe
