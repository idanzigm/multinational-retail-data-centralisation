import pandas as pd

class DataCleaning:
    @staticmethod
    def clean_user_data(user_data):
        """
        Clean the user data by handling NULL values, correcting date errors,
        fixing incorrectly typed values.

        Parameters:
        - user_data (pd.DataFrame): The input DataFrame containing user data.

        Returns:
        - pd.DataFrame: Cleaned user data.
        """
        cleaned_data = user_data.copy()

        # Handling NULL values
        cleaned_data = cleaned_data.dropna()

        # Correcting date errors
        cleaned_data['join_date'] = pd.to_datetime(cleaned_data['join_date'], errors='coerce')

        # Fixing incorrectly typed values
        cleaned_data['user_uuid'] = pd.to_numeric(cleaned_data['user_uuid'], errors='coerce')

        # The line below has been removed, so no filtering based on a condition
        # cleaned_data = cleaned_data[~(cleaned_data['condition_column'] == 'condition_value')]

        return cleaned_data
    
# import pandas as pd
# from database_utils import DatabaseConnector
# class DataCleaning:

#     def clean_user_data(user_data):
#         # Method to clean the user data
#         cleaned_data = user_data.copy()

#         # Handling NULL values
#         cleaned_data = cleaned_data.dropna()

#         # Correcting date errors (assuming 'date_column' is the date column in the DataFrame)
#         cleaned_data['opening_date'] = pd.to_datetime(cleaned_data['opening_date'], errors='coerce')

#         # Fixing incorrectly typed values
#         # (assuming 'numeric_column' is a numeric column in the DataFrame)
#         cleaned_data['numeric_column'] = pd.to_numeric(cleaned_data['numeric_column'], errors='coerce')

#         return cleaned_data
# #     def __init__(self):
# #         self.db_connector = DatabaseConnector()

# #     # T3S6: Create a method called clean_user_data which will perform the cleaning of the user data
# #     def clean_user_data(self, df):
# #         print(f"Type of df: {type(df)}")
# #         # Remove rows with NULL values
# #         cleaned_df = df.dropna()

# #         # Handle date errors 
# #         try:
# #             df['opening_date'] = pd.to_datetime(df['opening_date'], format='%Y-%m-%d')
# #         except ValueError as e:
# #             print(f"Error converting dates: {e}")
            
# #         return df
    
# #         self.db_connector.upload_to_db(cleaned_df, 'your_table_name')

# # data_cleaner = DataCleaning()
# # cleaned_df = data_cleaner.clean_user_data(df)