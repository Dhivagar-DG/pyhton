import mysql.connector


def get_db_connection():
    DBCON = mysql.connector.connect( host="127.0.0.1", user="username", password="password", port="3306",
                                     database="database name" )
    return DBCON


def execute_qry(qry, param=None):
    try:
        DBCON = get_db_connection()
        cursor = DBCON.cursor()
        res = cursor.execute(qry, param)
        DBCON.commit()
        DBCON.close()
        return res
    except:
        DBCON.rollback()
        DBCON.close()
        return False

def select_qry(qry, param=None):
    try:
        DBCON = get_db_connection()
        cur = DBCON.cursor()
        if param:
            cur.execute(qry, param)
            res = cur.fetchall()
        else:
            cur.execute(qry)
            res = cur.fetchall()
        DBCON.close()
        return res
    except Exception as e:
        print("DB ERROR : ", e)
        DBCON.close()
        return False


def add_new_user_data(name, age, city):
    QRY = "insert into users (name, age, city) values(%s, %s, %s);"
    execute_qry(QRY, (name, age, city))


def update_user_data(name, age, city, id):
    QRY = "update users set name=%s, age=%s, city=%s where user_id=%s;"
    execute_qry(QRY, (name, age, city, id))


def delete_user_data(id):
    QRY = "delete from users where user_id=%s;"
    execute_qry(QRY, (id,))


def get_user_data():
    QRY = "select * from users ;"
    return select_qry(QRY)

