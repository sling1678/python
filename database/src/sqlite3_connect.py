#!/usr/bin/python
'''
1. To connect to a database: sqlite3.connect(database [,timeout ,other optional arguments])
2. To make the transaction visible by everyone else: connection.commit()
3. To obtain total number of database rows that have been modified: connection.total_changes()
4. To close the connection: connection.close() - you must call commit BEFORE CLOSING for changes to occur
5. ** To roll back any changes sice las commit: connection.rollback()

6. To create a pointer to the selction from databse: connection.cursor([cursorClass])
7. To execute an dSQL command: cursor.execute(sql [, optional parameters])
8. To fetches the next row of a query result set: cursor.fetchone()
9. To fetch many: cursor.fetchmany([size = cursor.arraysize])
10. To fetch all: cursor.fetchall()

'''




## create table company
import sqlite3

# conn = sqlite3.connect('test.db')
# print("Opened database successfully")
#
# conn.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
# print("Table created successfully")
#
# conn.close()
# print("Closed database successfully")
# # insert data to table
# #!/usr/bin/python


# conn = sqlite3.connect('test.db')
# print("Opened database successfully")
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )")
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
#
# conn.commit()
# print("Records created successfully")
# conn.close()
# print("Closed database successfully")


# Read data from table

conn = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()
print("Closed database successfully")

##UPDATE
conn = sqlite3.connect('test.db')
print ("Opened database successfullyfor UPDATE")

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("UPDATE Operation done successfully")
conn.close()

# DELETE

#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute("DELETE from COMPANY where ID = 2;")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")
conn.close()

