import pandas as pd
from database_utils import DatabaseConnector

class DataExtractor:
    @staticmethod
    def read_rds_table(connector_instance, table_name):
        """
        Extract the database table to a pandas DataFrame.

        Parameters:
        - connector_instance: An instance of DatabaseConnector.
        - table_name (str): The name of the table to extract.

        Returns:
        - pd.DataFrame: Extracted data.
        """
        engine = connector_instance.init_db_engine()

        with engine.connect() as connection:
            query = f"SELECT * FROM {table_name};"
            return pd.read_sql(query, connection)


# import pandas as pd
# import requests
# import boto3
# import io
# from database_utils import DatabaseConnector

# # This calss will work as a utility class, in it will be methods that help extract data from different data sources. The methods contained will be fit to extract data from a particular data source, these sources will include CSV files, an API and an S3 bucket. 
# class DataExtractor:
#     @staticmethod
#     def extract_rds_data(table_name):
#         # Method to extract data from an AWS RDS database
#         engine = DatabaseConnector.init_db_engine()

#         # Use pandas to read data from the specified table
#         with engine.connect() as connection:
#             query = f"SELECT * FROM {table_name};"
#             data = pd.read_sql(query, connection)

#         return data

#     @staticmethod
#     def list_db_tables():
#         # Method to list all tables in the database
#         engine = DatabaseConnector.init_db_engine()

#         with engine.connect() as connection:
#             metadata = MetaData()
#             metadata.reflect(bind=connection)
#             table_names = metadata.tables.keys()

#         return table_names

#     @staticmethod
#     def read_rds_table(connector_instance, table_name):
#         # Method to extract the database table to a pandas DataFrame
#         tables = DataExtractor.list_db_tables()

#         if table_name not in tables:
#             raise ValueError(f"Table '{table_name}' not found in the database.")

#         data = connector_instance.extract_rds_data(table_name)
#         return data
#     def __init__(self):
#         pass

#     # T3S5: Create a method 'read_rds_table' which will extract the database table to a pandas DataFrame
#     def read_rds_table(self, db_connector, legacy_users):
#         engine = db_connector.init_db_engine()
#         query = f"SELECT * FROM {legacy_users}"
#         df = pd.read_sql(query, engine)
#         return df
        
    # def extract_from_csv(self, file_path):
    #     """
    #     Method to extract data from a CSV file.

    #     Args:
    #         file_path (str): Path to the CSV file.

    #     Returns:
    #         pd.DataFrame: Extracted data as a Pandas DataFrame.
    #     """
    #     try:
    #         df = pd.read_csv(file_path)
    #         return df
    #     except Exception as e:
    #         print(f"Error extracting data from CSV: {e}")
    #         return None
    
    # def extract_from_api(self, api_url):
    #     """
    #     Method to extract data from an API.

    #     Args:
    #         api_url (str): URL of the API.

    #     Returns:
    #         pd.DataFrame: Extracted data as a Pandas DataFrame.
    #     """
    #     try:
    #         response = requests.get(api_url)
    #         response.raise_for_status()  # Raise an error if the request was unsuccessful

    #         data = response.json()
    #         df = pd.DataFrame(data)
    #         return df
    #     except Exception as e:
    #         print(f"Error extracting data from API: {e}")
    #         return None
    
    # def extract_from_s3(self, bucket_name, file_key):
    #     """
    #     Method to extract data from an S3 bucket.

    #     Args:
    #         bucket_name (str): Name of the S3 bucket.
    #         file_key (str): Key (path) of the file within the bucket.

    #     Returns:
    #         pd.DataFrame: Extracted data as a Pandas DataFrame.
    #     """
    #     try:
    #         s3 = boto3.client('s3')
    #         response = s3.get_object(Bucket=bucket_name, Key=file_key)
    #         data = response['Body'].read().decode('utf-8')
    #         df = pd.read_csv(io.StringIO(data))
    #         return df
    #     except Exception as e:
    #         print(f"Error extracting data from S3: {e}")
    #         return None
