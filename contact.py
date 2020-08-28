import sqlite3

conn = sqlite3.connect("contct.db")
cursor = conn.cursor()

select = int(input(" 1 - Создать Новый контакт\n 2 - Просмотреть все контакты\n "))

if select == 1:
    nameContact = input("Name: ",)
    phoneContact = input("Phone: ",)
    emailContact = input("Email: ",)
    cursor.execute(
        """INSERT INTO contacts
        VALUES (?, ?, ?)
        """, (nameContact, phoneContact, emailContact)
    )
    conn.commit()
    print("Добавлено!")

elif select == 2:
    cursor.execute(
        """SELECT * FROM contacts
        """
    )
    conn.commit()
    print("---------------- Контакты ----------------\n", cursor.fetchall())

else:
    print("Такой комманды не существует")