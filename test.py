from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning


# Check database connection
try:
    conn = db_connector.connect_to_rds()
    print("Database connection successful!")
    conn.close()  # Close the connection after checking
except Exception as e:
    print(f"Error connecting to the database: {e}")

# Step 5: Read data from RDS database
db_connector = DatabaseConnector()
data_extractor = DataExtractor()
table_name = db_connector.list_db_tables()[0]  # Assuming the first table contains user data
user_data = data_extractor.read_rds_table(db_connector, table_name)
print(user_data)
print(user_data.columns)

# Example usage to upload data to a temporary table
try:
    temp_table_name = 'temp_upload_test'
    db_connector.upload_to_db(temp_table_name, cleaned_user_data)
    print(f"Data uploaded to '{temp_table_name}' successfully!")
except Exception as e:
    print(f"Error uploading data: {e}")


# Assuming 'user_table_name' is the table containing user data in the RDS database
user_data = DataExtractor.read_rds_table(db_connector, user_table_name)

# Clean the user data
cleaned_user_data = DataCleaning.clean_user_data(user_data)

# Specify the target table name
target_table_name = 'dim_users'

# Upload the cleaned user data to the sales_data database in the dim_users table
DatabaseConnector.upload_to_db(target_table_name, cleaned_user_data)