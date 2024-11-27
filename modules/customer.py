# Define a mapping dictionary for correcting customer names
CUSTOMER_NAME_MAP = {
    "WESHIP": "WESHIP",
    "WESHIIP": "WESHIP",
    "APEX": "APEX",
    "APEXS": "APEX",
    "BLUESTAR" : "BLUE STAR",
    "FOREST- SHENZHEN" : "FOREST-SHENZHEN",
    "FOREST- NINGBO" : "FOREST-NINGBO",
    "FOREST- CHANGSHA" : "FOREST-CHANGSHA",
    "FOREST - HUNAN" : "FOREST-HUNAN",
    "NINGBO NANHUA" : "NINGBO NANHUA",
    "RABBIT SPEED  兔兔及时达" : "RABBIT SPEED",
    "WING SHIP 厦门翼舟" : "WING SHIP"
    # Add other potential typo corrections
}
def clean_customer_column(customer_series):

    print("\nOriginal CUSTOMER column:")
    print(customer_series.unique())  # Print unique values before cleaning
    
    # Step 1: Ensure all values are strings
    customer_series = customer_series.astype(str)
    
    # Step 2: Strip whitespace
    customer_series = customer_series.str.strip()
    
    # Step 3: Convert to uppercase
    customer_series = customer_series.str.upper()
    
    # Step 4: Apply mapping
    customer_series = customer_series.replace(CUSTOMER_NAME_MAP)
    
    print("\nCleaned CUSTOMER column after mapping:")
    print(customer_series.unique())  # Print unique values after cleaning
    
    # Step 5: Handle missing or invalid values
    customer_series = customer_series.replace("NAN", "")  # Replace 'nan' strings
    customer_series = customer_series.fillna('')  # Fill actual NaN values
    
    return customer_series
