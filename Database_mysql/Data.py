import mysql.connector
from loguru import logger
class SQLConn:
    def __init__(self) -> None:
        pass
    
    def create_conn(self):
        conn = mysql.connector.connect(host='localhost',
                                 user ='root',
                                 passwd ='123456789',
                                 database = 'qlhs')
        return conn
