import sqlite3

# Create a connection to the database
connection=sqlite3.connect("student.db")

##Create a cursor object
cursor=connection.cursor()

##Create a table
table_info="""
CREATE TABLE student(name varchar(25), class varchar(25),
section varchar(25), roll_no int, marks int)
"""

cursor.execute(table_info)

##insert some more records
cursor.execute("INSERT INTO student VALUES('John','Data Science','A',101,90)")
cursor.execute("INSERT INTO student VALUES('Sam','Data Science','B',102,85)")
cursor.execute("INSERT INTO student VALUES('Tom','Data Analysis','C',103,80)")
cursor.execute("INSERT INTO student VALUES('Jerry','DevOps','D',104,75)")
cursor.execute("INSERT INTO student VALUES('Tim','Testing','E',105,70)")

##Display the records
print("The insertes rows are ")

data=cursor.execute("SELECT * FROM student")

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()

print("Connection closed")



