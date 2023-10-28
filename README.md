# Overview

A test for implementing python SQLite3 code for CRUD operations on a simple database.

Follow the prompted inputs to view, insert, update, and delete data from the database.

[Software Demo Video](https://youtu.be/wP0EWSAC-iM)

# Relational Database

SQLite database.

The database manipulated is the goblinpedia, a comical database cataloging goblins.
It has two tables.

monsters:

- monsterId (autoincrementing integer)
- monsterName (unique text)
- monsterDescription (text)
- monsterHealth (integer)
- monsterWeapon (text)

weapons:

- weaponId (autoincrementing integer)
- weaponName (unique text)
- weaponDamage (integer)

# Development Environment

Database created using SQLite3 and SQLiteStudio.

Python code made in Visual Studio Code, and using the SQLite3 library.

# Useful Websites

- [sqlitetutorial.net](https://www.sqlitetutorial.net/)
- [python.org](https://docs.python.org/3.8/library/sqlite3.html)
- [w3schools.com/sql](https://www.w3schools.com/sql/default.asp)

# Future Work

- present selected data in more visually pleasing way.
- make delete prompts more secure (accepts SQL injections)
- catch data type errors
