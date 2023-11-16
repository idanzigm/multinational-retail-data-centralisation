import yaml
import psycopg2
from sqlalchemy import create_engine

class DatabaseConnector:
    def __init__(self, database_name, user, password, host, port):
        self.database_name = database_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
    
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
    
    # Create a method 'read_db_creds'
    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as file:
            creds = yaml.safe_load(file)
        return creds

    # Create a method 'init_db_engine'
    def init_db_engine(self):
        creds = self.read_db_creds()
        connection_string = f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        engine = create_engine(connection_string)
        return engine
    
    # Create a method 'list_db_tables'
    def list_db_tables(self):
        engine = self.init_db_engine()
        inspector = inspect(engine)
        return inspector.get_table_names()
    
    # Create a method to 'uplodad_to_db'
    def upload_to_db(self, df, table_name):
        engine = self.init_db_engine()
        df.to_sql(table_name, engine, if_exists='replace', index=False)