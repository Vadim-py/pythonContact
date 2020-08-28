import sqlite3

conn = sqlite3.connect("contct.db")
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE contacts
       (name, phone, email)
    """
)