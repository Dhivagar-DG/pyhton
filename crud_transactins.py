import sqlite3
import os

# DB CONNECTION
DBPATH = "C:\\Users\\DHIVAGAR\\Documents\\DB"
DB = os.path.join( DBPATH, "CRUD.db" )


# DATABASE CLASS
class CrudDataBase:
    def __init__(self):
        self.DBCON = None

    def get_db_connection(self):
        self.DBCON = sqlite3.Connection( DB )

    def close_db_connection(self):
        self.DBCON.close()

    # DB TANSACTION
    def insertQRY(self, name, age, city):
        try:
            self.get_db_connection()
            QRY = "insert into Users (uName,Age,City) values (?,?,?);"
            self.DBCON.execute( QRY, (name, age, city) )
            self.DBCON.commit()
        except:
            self.DBCON.rollback()

    def updateQRY(self, name, age, city, id):
        try:
            self.get_db_connection()
            QRY = "update Users set uName=?, Age=?, City=? where ID=?;"
            self.DBCON.execute( QRY, (name, age, city, id) )
            self.DBCON.commit()
        except:
            self.DBCON.rollback()

    def deleteQRY(self, id):
        try:
            self.get_db_connection()
            QRY = "delete from Users where ID=?;"
            self.DBCON.execute( QRY, (id,) )
            self.DBCON.commit()
            self.selectQRY()
        except:
            self.DBCON.rollback()

    def selectQRY(self):
        self.get_db_connection()
        QRY = "Select * from Users;"
        usersData = self.DBCON.execute( QRY )
        return usersData
