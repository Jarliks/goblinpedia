import sqlite3

connection = sqlite3.connect('.\db\goblinpedia.db')
cursor = connection.cursor()


print("Would you like to INSERT new data, DELETE data, UPDATE existing data, VIEW monster table, or view JOINED monster and weapon tables?")
buffer = ""
while True:
    line = input()
    if line == "":
        break
    buffer += line

    # INSERT
    if line.lower() == "insert":
        name = input("What is the monster's name? ")
        description = input("What is the description of the monster? ")
        health = input("What is the monster's health poits? ")
        weapon = input("What is the monster's Weapon? ")
        insertValues = (str(name), str(description), int(health), str(weapon))
        cursor.execute('INSERT INTO monsters (monsterName, monsterDescription, monsterHealth, monsterWeapon) VALUES (?, ?, ?, ?);', insertValues)
        connection.commit()
        print("Row inserted.")

    # DELETE
    elif line.lower() == "delete":
        deleteValues = input("What is the ID of the monster you would like to delete? ")
        cursor.execute(f'DELETE FROM monsters WHERE monsterId = {deleteValues};')
        connection.commit()
        print("Row deleted.")

    # UPDATE
    elif line.lower() == "update":
        oldName = input("What is the name of the monster you would like to update? ")
        name = input("What is the monster's updated name? ")
        description = input("What is the updated description of the monster? ")
        health = input("What is the monster's updated health points? ")
        weapon = input("What is the monster's updated Weapon? ")
        updateValues = (str(name), str(description), int(health), str(weapon), str(oldName))
        cursor.execute('UPDATE monsters SET monsterName = ?, monsterDescription = ?, monsterHealth = ?, monsterWeapon = ? WHERE monsterName = ?;', updateValues)
        connection.commit()
        print("Row updated.")

    # SELECT
    elif line.lower() == "view":
        cursor.execute('SELECT * FROM monsters;')
        for row in cursor.fetchall():
            print(row)
        connection.commit()

    elif line.lower() == "joined":
        cursor.execute('SELECT monsterName, monsterDescription, monsterHealth, monsterWeapon, weaponDamage FROM monsters JOIN weapons ON monsters.monsterWeapon = weapons.weaponName;')
        for row in cursor.fetchall():
            print(row)
        connection.commit()

    else:
        print("Invalid command, please try again.")

connection.close()