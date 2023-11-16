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


    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as file:
            creds = yaml.safe_load(file)
        return creds


DatabaseConnector.read_db_creds(self)