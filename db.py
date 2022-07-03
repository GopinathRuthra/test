import sqlite3  
  
con = sqlite3.connect("asset.db")  
print("Database opened successfully")  
  
con.execute("create table details (id INTEGER PRIMARY KEY AUTOINCREMENT, GID TEXT NOT NULL, Emp_Name TEXT NOT NULL, Band TEXT NOT NULL, CCName TEXT NOT NULL, CCID TEXT NOT NULL, DOJ TEXT NOT NULL, W_Email TEXT NOT NULL, Manager TEXT NOT NULL, Band_Change_Date TEXT NOT NULL, Lead TEXT NOT NULL, AGM_VP TEXT NOT NULL, Job_Role TEXT NOT NULL, T_Name TEXT NOT NULL, SPOC TEXT NOT NULL, Core_Process TEXT NOT NULL, Sub_Process TEXT NOT NULL, Higher_Qualification TEXT NOT NULL, GENDER TEXT, DOB TEXT NOT NULL, Work_Location TEXT NOT NULL, P_Team TEXT NOT NULL, Vaccine_Action_Plan TEXT NOT NULL, Vaccinated_Status TEXT NOT NULL, Vaccination_Certificate_Uploaded TEXT NOT NULL, Accomodation TEXT NOT NULL, Personal_Email TEXT NOT NULL, Insurance TEXT NOT NULL, ECName TEXT NOT NULL, ECNumber TEXT NOT NULL, Mob TEXT NOT NULL, Marital TEXT NOT NULL, Transport TEXT NOT NULL, Distance TEXT NOT NULL, Pickup TEXT NOT NULL, Address TEXT NOT NULL, City_Pin TEXT NOT NULL, Native_District TEXT NOT NULL, Native_State TEXT NOT NULL, Type_of_Asset TEXT NOT NULL, CPU_Laptop TEXT NOT NULL, Docking_Station TEXT NOT NULL, Monitor_1 TEXT NOT NULL, Monitor_2  TEXT NOT NULL, Desk_No TEXT NOT NULL, Dual_Moniter_SetUp TEXT NOT NULL, Internet_availability TEXT NOT NULL, Head_Phone_availability TEXT NOT NULL, Additional_Key_Board TEXT NOT NULL, Mouse TEXT NOT NULL, UPS TEXT NOT NULL, Proper_Table_availability TEXT NOT NULL, Proper_Chair_availability TEXT NOT NULL, Spike_Buster TEXT NOT NULL) " )  

con.row_factory = sqlite3.Row

cur = con.cursor() 

cur.execute("SELECT * FROM details")

result = cur.execute("SELECT * FROM details")
print(cur.fetchall())
cur.close()
print("Table created successfully")  
  
con.close()