import sqlite3

con=sqlite3.connect("student.db");
print("Database created successfully");


con.execute("create table Student(roll_no integer primary key autoincrement,name text not null,percentage float not null)");
print("Table created successfully");

con.close();