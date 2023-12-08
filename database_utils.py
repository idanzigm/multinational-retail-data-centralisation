import psycopg2
from sqlalchemy import create_engine, MetaData
import yaml

class DatabaseConnector:
    def __init__(self):
        pass

    @staticmethod
    def read_db_creds():
        """
        Read the credentials from the YAML file.

        Returns:
        - dict: Database credentials.
        """
        with open("db_creds.yaml", "r") as yaml_file:
            creds = yaml.safe_load(yaml_file)
        return creds

    @staticmethod
    def init_db_engine():
        """
        Initialize and return an SQLAlchemy database engine.

        Returns:
        - sqlalchemy.engine.base.Engine: Database engine.
        """
        creds = DatabaseConnector.read_db_creds()

        db_url = f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        engine = create_engine(db_url)

        return engine

    def list_db_tables(self):
        """
        List all tables in the database.

        Returns:
        - list: List of table names.
        """
        engine = self.init_db_engine()

        with engine.connect() as connection:
            metadata = MetaData()
            metadata.reflect(bind=connection)
            table_names = metadata.tables.keys()

        return list(table_names)

    def upload_to_db(self, table_name, data):
        """
        Upload data to the specified table in the database.

        Parameters:
        - table_name (str): The name of the target table.
        - data (pd.DataFrame): Data to be uploaded.
        """
        engine = self.init_db_engine()

        with engine.connect() as connection:
            data.to_sql(table_name, connection, index=False, if_exists='replace')
# import yaml
# from sqlalchemy import create_engine, MetaData
# import pandas as pd
# import psycopg2
# import yaml

# class DatabaseConnector:

#     def __init__(self, creds_file_path='db_creds.yaml'):
#         self.credentials = self.read_db_creds(creds_file_path)
#         self.connection = None
#         self.cursor = None

#     def read_db_creds(self, creds_file_path):
#         # Method to read database credentials from a YAML file and return a dictionary
#         try:
#             with open(creds_file_path, 'r') as file:
#                 creds = yaml.safe_load(file)
#             return creds
#         except Exception as e:
#             print(f"Error: Unable to read database credentials.\n{str(e)}")
#             return {}

#     def connect(self):
#         # Method to establish a connection to the RDS database
#         try:
#             self.connection = psycopg2.connect(**self.credentials)
#             self.cursor = self.connection.cursor()
#             print("Connected to the RDS database.")
#         except Exception as e:
#             print(f"Error: Unable to connect to the RDS database.\n{str(e)}")

#     def close_connection(self):
#         # Method to close the RDS database connection
#         if self.connection:
#             self.connection.close()
#             print("Connection to the RDS database closed.")


#     def init_db_engine(self):
#         # Method to initialize and return an SQLAlchemy database engine
#         try:
#             engine = create_engine(
#                 f"postgresql+psycopg2://{self.credentials['user']}:{self.credentials['password']}@{self.credentials['host']}:{self.credentials['port']}/{self.credentials['dbname']}",
#                  echo=True  # Set to False for production
#             )
#             print("Database engine initialized.")
#             return engine
#         except Exception as e:
#             print(f"Error: Unable to initialize the database engine.\n{str(e)}")
#             return None
    
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
#     def upload_to_db(table_name, data):
#         # Method to upload a Pandas DataFrame to the specified table in the database
#         engine = DatabaseConnector.init_db_engine()

#         with engine.connect() as connection:
#             data.to_sql(table_name, connection, index=False, if_exists='replace')
    
# #     def __init__(self, creds_file_path='db_creds.yaml'):
# #         self.credentials = self.read_db_creds(creds_file_path)
# #         self.connection = None
# #         self.cursor = None

# #     def read_db_creds(self, creds_file_path):
# #         # Method to read database credentials from a YAML file and return a dictionary
# #         try:
# #             with open(creds_file_path, 'r') as file:
# #                 creds = yaml.safe_load(file)
# #             return creds
# #         except Exception as e:
# #             print(f"Error: Unable to read database credentials.\n{str(e)}")
# #             return {}

# #     def connect(self):
# #         # Method to establish a connection to the RDS database
# #         try:
# #             self.connection = psycopg2.connect(**self.credentials)
# #             self.cursor = self.connection.cursor()
# #             print("Connected to the RDS database.")
# #         except Exception as e:
# #             print(f"Error: Unable to connect to the RDS database.\n{str(e)}")

# #     def close_connection(self):
# #         # Method to close the RDS database connection
# #         if self.connection:
# #             self.connection.close()
# #             print("Connection to the RDS database closed.")


# #     def init_db_engine(self):
# #         # Method to initialize and return an SQLAlchemy database engine
# #         try:
# #             engine = create_engine(
# #                 f"postgresql+psycopg2://{self.credentials['user']}:{self.credentials['password']}@{self.credentials['host']}:{self.credentials['port']}/{self.credentials['dbname']}",
# #                  echo=True  # Set to False for production
# #             )
# #             print("Database engine initialized.")
# #             return engine
# #         except Exception as e:
# #             print(f"Error: Unable to initialize the database engine.\n{str(e)}")
# #             return None
        
# #     def list_db_tables(self, engine):
# #         # Method to list all tables in the database
# #         try:
# #             inspector = inspect(engine)
# #             table_names = inspector.get_table_names()
# #             print("Tables in the database:")
# #             for table_name in table_names:
# #                 print(table_name)
# #             return table_names
# #         except Exception as e:
# # #             print(f"Error: Unable to list tables in the database.\n{str(e)}")
# # #             return []

# # class DatabaseConnector:

# #     def __init__(self, creds_file_path='db_creds.yaml'):
# #         self.credentials = self.read_db_creds(creds_file_path)
# #         self.connection = None
# #         self.cursor = None
# #         self.engine = self.init_db_engine()
# #         pass
    
# #     # T3S2: Create a method 'read_db_creds'
# #     def read_db_creds(self, creds_file_path):
# #         try:
# #             with open(creds_file_path, 'r') as file:
# #                 creds = yaml.safe_load(file)
# #                 return {
# #                     'dbname': creds['RDS_DATABASE'],
# #                     'user': creds['RDS_USER'],
# #                     'password': creds['RDS_PASSWORD'],
# #                     'host': creds['RDS_HOST'],
# #                     'port': creds['RDS_PORT']
# #                 }
# #         except Exception as e:
# #             print(f"Error: Unable to read database credentials.\n{str(e)}")
# #             return {}

# #     # T3S3: Create a method 'init_db_engine' that will read the credentials from the return of read_db_creds and initialise and return an sqlalchemy database engine.
# #     def init_db_engine(self):
# #         try:
# #             engine = create_engine(
# #                 f"postgresql+psycopg2://{self.credentials['user']}:{self.credentials['password']}@{self.credentials['host']}:{self.credentials['port']}/{self.credentials['dbname']}",
# #                 echo=True  # Set to False for production
# #             )
# #             print("Database engine initialized.")
# #             return engine
# #         except Exception as e:
# #             print(f"Error: Unable to initialize the database engine.\n{str(e)}")
# #             return None
    
# #     # T3S5: Create a method 'list_db_tables' to list all the tables in the database to know which tables to extract from. 
# #     def list_db_tables(self):
# #         try:
# #             inspector = inspect(self.engine)
# #             return inspector.get_table_names()
# #         except Exception as e:
# #             print(f"Error: Unable to list tables in the database.\n{str(e)}")
# #             return []
    
# #     # T3S7: Create a method to 'upload_to_db' This method will take in a Pandas DataFrame and table name to upload to as an argument
# #     def upload_to_db(self, df, legacy_users):
# #         try:
# #             df.to_sql(table_name, self.engine, if_exists='replace', index=False)
# #             print(f"Data uploaded to table '{table_name}'.")
# #         except Exception as e:
# #             print(f"Error: Unable to upload data to the database.\n{str(e)}")

        
# #     # def connect(self):
# #     #     try:
# #     #         self.connection = psycopg2.connect(
# #     #             database=self.database_name,
# #     #             user=self.user,
# #     #             password=self.password,
# #     #             host=self.host,
# #     #             port=self.port
# #     #         )
# #     #         print("Connected to database successfully")
# #     #     except Exception as e:
# #     #         print(f"Error connecting to database: {e}")
    
# #     # def upload_data(self, data, table_name):
# #     #     # Method to upload data to the database
# #     #     pass
    
# #     # def disconnect(self):
# #     #     if self.connection:
# #     #         self.connection.close()
# #     #         print("Disconnected from database")
# #     #     else:
# #     #         print("No active database connection")

# #         # def __init__(self):
# #     #     pass
