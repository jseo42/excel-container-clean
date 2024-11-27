SSL_NAME_MAP = {
    "COSCO": "COSCO",
    "CSCO": "COSCO",
    "HMM": "HMM",
    "ONE": "ONE",
    "MSC": "MSC",
    # Add more mappings as needed
}

def clean_ssl_column(ssl_series):

    print("\nOriginal SSL column unique values:")
    print(ssl_series.dropna().unique())  # Print unique non-NaN values before cleaning
    
    # Step 1: Strip whitespace
    ssl_series = ssl_series.str.strip()
    
    # Step 2: Convert to uppercase
    ssl_series = ssl_series.str.upper()
    
    # Step 3: Replace typos based on the mapping
    ssl_series = ssl_series.replace(SSL_NAME_MAP)
    
    # Step 4: Handle missing values
    ssl_series = ssl_series.fillna("")
    
    print("\nCleaned SSL column unique values:")
    print(ssl_series.unique())  # Print unique values after cleaning
    
    return ssl_series
