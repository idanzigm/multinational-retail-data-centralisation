from database_utils import DatabaseConnector
from database_utils import LocalDataBaseConnector 
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

def main():
    # Create an instance of DatabaseConnector
    db_connector = DatabaseConnector()

    # Assuming 'user_table_name' is the table containing user data in the RDS database
    user_data = DataExtractor.read_rds_table(db_connector, 'legacy_users')

    # Clean the user data
    cleaning_user_data = DataCleaning.clean_user_data(user_data)

    # Create an instance of DatabaseConnector
    local_db_connector = LocalDatabaseConnector()
    
    # Specify the target table name
    target_table_name = 'dim_users'

    # Upload the cleaned user data to the sales_data database in the dim_users table
    local_db_connector.upload_to_db(target_table_name, cleaning_user_data)

if __name__ == "__main__":
    main()
    # # Step 4: List all tables in the database
    # try:
    #     table_names = db_connector.list_db_tables()
    #     print("Tables in the database:")
    #     for table in table_names:
    #         print(f"- {table}")

    #     # Prompt user to enter the correct user table name
    #     user_table_name = input("\nEnter the name of the user table: ")

    #     user_data = DataExtractor.read_rds_table(db_connector, user_table_name)

    #     # Print columns of the user table
    #     print(f"\nColumns of the {user_table_name} table:")
    #     print(user_data.columns)

    #     # Clean the user data
    #     cleaned_user_data = DataCleaning.clean_user_data(user_data)

    #     # Specify the target table name
    #     target_table_name = 'dim_users'

    #     # Upload the cleaned user data to the sales_data database in the dim_users table
    #     db_connector.upload_to_db(target_table_name, cleaned_user_data)
        
    #     print(f"\nData successfully uploaded to the {target_table_name} table.")

    # except Exception as e:
    #     print(f"Error: {e}")



# from data_extraction import DataExtractor
# from data_cleaning import DataCleaning
# from database_utils import DatabaseConnector

# # Step 5: Read data from RDS database
# db_connector = DatabaseConnector()
# data_extractor = DataExtractor()
# table_name = db_connector.list_db_tables()[0]  # Assuming the first table contains user data
# user_data = data_extractor.read_rds_table(db_connector, table_name)
# print(user_data)
# print(user_data.columns)

# # Step 6: Clean the user data
# data_cleaner = DataCleaning()
# cleaned_user_data = data_cleaner.clean_user_data(table_name)

# # Step 8: Upload cleaned data to the database
# table_to_upload = 'legacy_users'
# db_connector.upload_to_db(cleaned_user_data, table_name)
