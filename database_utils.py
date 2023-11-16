import yaml
from sqlalchemy import create_engine, inspect
import pandas as pd


class DatabaseConnector:
    # def __init__(self):
    #     pass
    # def __init__(self, database_name, user, password, host, port):
    #     self.database_name = database_name
    #     self.user = user
    #     self.password = password
    #     self.host = host
    #     self.port = port
    #     self.connection = None
    
    # T3S2: Create a method 'read_db_creds'
    def read_db_creds(self, creds_file_path='db_creds.yaml'):
        with open(creds_file_path, 'r') as file:
            creds = yaml.safe_load(file)
        return creds

    # T3S3: Create a method 'init_db_engine' that will read the credentials from the return of read_db_creds and initialise and return an sqlalchemy database engine.
    def init_db_engine(self):
        creds = self.read_db_creds()
        connection_string = f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        engine = create_engine(connection_string)
        return engine
    
    # T3S5: Create a method 'list_db_tables' to list all the tables in the database to know which tables to extract from. 
    def list_db_tables(self):
        engine = self.init_db_engine()
        inspector = inspect(engine)
        return inspector.get_table_names()
    
    # T3S7: Create a method to 'upload_to_db' This method will take in a Pandas DataFrame and table name to upload to as an argument
    def upload_to_db(self, df, table_name):
        engine = self.init_db_engine()
        df.to_sql(table_name, engine, if_exists='replace', index=False)

        
    # def connect(self):
    #     try:
    #         self.connection = psycopg2.connect(
    #             database=self.database_name,
    #             user=self.user,
    #             password=self.password,
    #             host=self.host,
    #             port=self.port
    #         )
    #         print("Connected to database successfully")
    #     except Exception as e:
    #         print(f"Error connecting to database: {e}")
    
    # def upload_data(self, data, table_name):
    #     # Method to upload data to the database
    #     pass
    
    # def disconnect(self):
    #     if self.connection:
    #         self.connection.close()
    #         print("Disconnected from database")
    #     else:
    #         print("No active database connection")