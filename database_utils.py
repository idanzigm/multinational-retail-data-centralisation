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