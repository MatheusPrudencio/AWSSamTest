import json

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String, MetaData, Integer


class DB:
    def __init__(self, user, password, host, db_ousadia):
        self.user = user
        self.password = password
        self.host = host
        self.db_ousadia =  db_ousadia

        db_string = "mysql+pymysql://{}:{}@{}/{}".format(
            self.user, 
            self.password, 
            self.host,
            self.db_ousadia
        )

        self.db = create_engine(db_string)
        meta = MetaData()
        self.Base = declarative_base()
    
        user = Table(
            'foiPorra', meta, 
            Column('id', Integer, primary_key = True), 
            Column('name', String), 
        )

        select_user = user.select()
        conn = self.db.connect()
        result = conn.execute(select_user)
        print(result)

        for row in result:
            print (row)

def init():
    db_instance = DB(
        user='test', 
        password='password',    
        host='172.18.0.1', 
        db_ousadia='Exemple'
    )

if __name__ == "__main__":
    # execute only if run as a script
    init()

def lambda_handler(event, context):
    h = init()
    print(h)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('All tables have been created')
    }
