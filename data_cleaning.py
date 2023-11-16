class DataCleaning:

    def __init__(self):
        pass

    # T3S6: Create a method called clean_user_data which will perform the cleaning of the user data
    def clean_user_data(self, df):
        # Remove rows with NULL values
        df = df.dropna()

        # Handle date errors (assuming date_column is the column containing dates)
        try:
            df['date_column'] = pd.to_datetime(df['date_column'], format='%Y-%m-%d')
        except ValueError as e:
            print(f"Error converting dates: {e}")

        # Handle incorrectly typed values (assuming int_column should be integers)
        try:
            df['int_column'] = df['int_column'].astype(int)
        except ValueError as e:
            print(f"Error converting to integers: {e}")

        # Handle rows filled with wrong information based on some condition
        df = df[df['condition_column'] == 'desired_condition']

        return df
    
    # def clean_csv_data(self, data):
    #     # Method to clean data extracted from a CSV file
    #     pass
    
    # def clean_api_data(self, data):
    #     # Method to clean data extracted from an API
    #     pass
    
    # def clean_s3_data(self, data):
    #     # Method to clean data extracted from an S3 bucket
    #     pass