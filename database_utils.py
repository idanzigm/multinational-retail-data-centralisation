import yaml
import psycopg2
from sqlalchemy import create_engine

class DatabaseConnector:
    def __init__(self, database_name, user, password, host, port):
        # Constructor to initialize database connection parameters
        pass
    
    def connect(self):
        # Method to establish a connection to the database
        pass
    
    def upload_data(self, data, table_name):
        # Method to upload data to the database
        pass
    
    def disconnect(self):
        # Method to close the database connection
        pass

    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as file:
            creds = yaml.safe_load(file)
        return creds
    
    from sqlalchemy import create_engine

    def init_db_engine(self):
        creds = self.read_db_creds()
        connection_string = f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        engine = create_engine(connection_string)
        return engine