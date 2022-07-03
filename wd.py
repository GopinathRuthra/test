import sqlite3  
  
con = sqlite3.connect("workday.db")  
print("Database opened successfully")  
  
con.execute("create table Employee_Details (id INTEGER PRIMARY KEY AUTOINCREMENT, GID TEXT NOT NULL, Emp_Name TEXT NOT NULL, Band TEXT NOT NULL, CCName TEXT NOT NULL, CCID TEXT NOT NULL, DOJ TEXT NOT NULL, W_Email TEXT NOT NULL, Manager TEXT NOT NULL, Band_Change_Date TEXT NOT NULL) " )  
  
print("Table created successfully")  

con.close()