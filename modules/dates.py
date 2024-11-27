import pandas as pd

def clean_date_column(date_series, column_name):
    print(f"\nProcessing column: {column_name}")
    
    # Step 1: Strip whitespace and handle NaN
    date_series = date_series.astype(str).str.strip()
    date_series = date_series.replace(['nan', 'None', '', 'N/A'], None)  # Replace invalid placeholders with None

    # Step 2: Preprocess partial and inconsistent dates
    def preprocess_date(date):
        if pd.isna(date) or date is None or date == "":
            return None
        if "/" in date and len(date.split("/")) == 2:  # Format: MM/DD
            return f"{date}/2024"  # Assume year 2024
        if "-" in date:  # Format: DD-MMM (e.g., 29-sep)
            return f"{date}-2024"  # Assume year 2024
        return date  # Return as-is for further parsing

    date_series = date_series.apply(preprocess_date)

    # Step 3: Parse dates
    date_series = pd.to_datetime(date_series, errors="coerce", format=None)

    # Step 4: Convert valid dates to MM/DD strings
    date_series = date_series.dt.strftime("%m/%d")  # Converts valid dates to MM/DD strings
    
    # Step 5: Replace invalid or missing dates with "UNKNOWN"
    date_series = date_series.fillna("")

    print(f"\nCleaned values for {column_name}:")
    print(date_series.head())
    
    return date_series
