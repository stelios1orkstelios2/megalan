from distutils.cmd import Command
import mysql.connector

# Very sneaky password 
f = open('password.txt', 'r')
p = f.readline()




class MyDB():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user='root',
            password=p,
            database='users'
        )
        self.cur = self.mydb.cursor(buffered=True)
    
    def query_with_parameter(self, selection, table, parameter):

        self.cur.execute(f"SELECT {selection} FROM {table} WHERE {parameter}")
        print("executed query command")
        self.cur.close()
        print('cursor connection closed')
    
    def query(self, selection, table):

        self.cur.execute(f"SELECT {selection} FROM {table}")
        print("executed query command")
        self.cur.close()
        print('cursor connection closed')
