def clean_cntr_column(cntr_series):
    print("\nOriginal CNTR# column:")
    print(cntr_series.head())
    
    # Step 1: Ensure all values are strings
    cntr_series = cntr_series.astype(str)
    
    # Step 2: Strip whitespace
    cntr_series = cntr_series.str.strip()
    
    # Step 3: Convert to uppercase
    cntr_series = cntr_series.str.upper()
    
    print("\nCleaned CNTR# column:")
    print(cntr_series)
    return cntr_series
