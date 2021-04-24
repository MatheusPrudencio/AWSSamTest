import json

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData


class DB:
    def __init__(self, user, password, host, port):
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        db_string = "postgres+pydataapi://{}:{}@{}:{}".format(
            self.user, 
            self.password, 
            self.host, 
            self.port
        )

        self.db = create_engine(db_string)

        self.meta = MetaData(self.db)

        self.user_table = Table(
            'users', self.meta,
            Column('email', String, primary_key=True),
            Column('name', String),
            Column('surname', String),
            Column('password', String),
            Column('salt', String)
        )

    def create_tables(self):
        self.meta.create_all(self.db)

        return True

def lambda_handler(event, context):
    db_instance = DB(
        user='testdock', 
        password='password', 
        host='localhost', 
        port=5432
    )
    
    db_instance.create_tables()
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('All tables have been created')
    }
