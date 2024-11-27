SIZE_MAP = {
    "40 HQ": "40HQ",
    "40 H-Q": "40HQ",
    "20 GP": "20GP",
    "20-GP": "20GP",
    "40 GP": "40GP",  # Add more corrections as needed
}

def clean_size_column(size_series):
    print("\nOriginal SIZE column:")
    print(size_series.unique())  # Display unique values before cleaning
    
    # Step 1: Strip whitespace
    size_series = size_series.str.strip()
    
    # Step 2: Convert to uppercase
    size_series = size_series.str.upper()
    
    # Step 3: Correct typos based on the mapping
    size_series = size_series.replace(SIZE_MAP)
    
    # Step 4: Handle missing or invalid values
    size_series = size_series.fillna("")
    
    print("\nCleaned SIZE column:")
    print(size_series.unique())  # Display unique values after cleaning
    
    return size_series
