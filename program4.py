import sqlite3

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Entries (name TEXT PRIMARY KEY,phone TEXT NOT NULL)')
conn.commit()

def add_entry():
    name = input('enter name: ')
    phone = input('enter phone number: ')
    try:
        cursor.execute("INSERT INTO Entries (name, phone) VALUES (?,?)", (name, phone))
        print ('entry added')
    except sqlite3.IntegrityError:
        print('entry already exists')
    conn.commit()

def find_entry():
    name = input('enter name to search: ')
    cursor.execute("SELECT phone FROM Entries WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        print(f"{name}'s phone number is {result[0]}")
    else:
        print("Entry not found.")

def update_entry():
    name = input('enter name to update: ')
    new_phone = input('enter new phone number: ')

    cursor.execute("UPDATE Entries SET phone = ? WHERE name = ?", (new_phone, name))

    if cursor.rowcount == 0:
        print("Entry not found.")
    else:
        conn.commit()
        print("phone number updated.")

def delete_entry():
    name = input('enter name to delete: ')
    cursor.execute("DELETE FROM Entries WHERE name = ?", (name,))

    if cursor.rowcount == 0:
        print("Entry not found.")
    else:
        conn.commit()
        print("entry deleted.")

def main():
    while True:
        print('\nphonebook menu')
        print('1. add entry')
        print('2. find entry')
        print('3. update entry')
        print('4. delete entry')
        print('5. exit')

        choice = int(input('enter your choice: '))
        if choice == 1:
            add_entry()
        elif choice == 2:
            find_entry()
        elif choice == 3:
            update_entry()
        elif choice == 4:
            delete_entry()
        elif choice == 5:
            break
        else:
            print('invalid choice')

    conn.close()

if __name__ == '__main__':
    main()

