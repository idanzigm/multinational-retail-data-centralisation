from data_extraction import DataExtractor
from data_cleaning import DataCleaning
from database_utils import DatabaseConnector

# Step 1: Initialize objects
extractor = DataExtractor()
cleaner = DataCleaning()
connector = DatabaseConnector()

# Step 2: Extract data from RDS database
user_data_df = extractor.read_rds_table(connector, 'user_data')

# Step 3: Clean user data
cleaned_user_data = cleaner.clean_user_data(user_data_df)

# Step 4: Upload cleaned data to the database
connector.upload_to_db(cleaned_user_data, 'dim_users')
