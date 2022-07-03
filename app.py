from os import name
from flask import Flask, render_template, json, request, redirect, url_for, flash, jsonify
from datetime import datetime
import sqlite3
  
app = Flask(__name__)

app.secret_key = "caircocoders-ednalan-2020"
   
@app.route('/')
def homepage():
    return render_template("/Front.html")
    
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/display')
def display():
    con = sqlite3.connect("asset.db")
    cur = con.cursor()  
    cur.execute("SELECT * FROM details")  
    rows = cur.fetchall()  
    return render_template("display.html", rows = rows) 


@app.route('/display', methods=['POST','GET'])
def adddisplay():
    rows = list()
    if request.method=="POST":
        a=request.form.get('GID')
        b=request.form.get('Emp_Name')
        c=request.form.get('Band')
        d=request.form.get('CCName')
        e=request.form.get('CCID')
        f=request.form.get('DOJ')
        g=request.form.get('W_Email')
        h=request.form.get('Manager')
        i=request.form.get('Band_Change_Date')
        j=request.form.get('Lead')
        k=request.form.get('AGM_VP')
        l=request.form.get('Job_Role')
        m=request.form.get('T_Name')
        if not m:
            m = "Not Applicable"
        n=request.form.get('SPOC')
        o=request.form.get('Core_Process')
        p=request.form.get('Sub_Process')
        q=request.form.get('Higher_Qualification')
        r=request.form.get('GENDER')
        s=request.form.get('DOB')
        t=request.form.get('Work_Location')
        u=request.form.get('P_Team')
        if not u:
            u = "Not Applicable"
        v=request.form.get('Vaccine_Action_Plan')
        w=request.form.get('Vaccinated_Status')
        x=request.form.get('Vaccination_Certificate_Uploaded')
        y=request.form.get('Accomodation')
        z=request.form.get('Personal_Email')
        a1=request.form.get('Insurance')
        b1=request.form.get('ECName')
        c1=request.form.get('ECNumber')
        d1=request.form.get('Mob')
        e1=request.form.get('Marital')
        f1=request.form.get('Transport')
        g1=request.form.get('Distance')
        h1=request.form.get('Pickup')
        if not h1:
            h1 = "Not Applicable"
        i1=request.form.get('Address')
        j1=request.form.get('City_Pin')        
        k1=request.form.get('Native_State')
        l1=request.form.get('Native_District')
        m1=request.form.get('Type_of_Asset')
        n1=request.form.get('CPU_Laptop')
        if not n1:
            n1 = "Not Applicable"
        o1=request.form.get('Docking_Station')
        if not o1:
            o1 = "Not Applicable"
        p1=request.form.get('Monitor_1')
        if not p1:
            p1 = "Not Applicable"
        q1=request.form.get('Monitor_2')
        if not q1:
            q1 = "Not Applicable"
        r1=request.form.get('Desk_No')
        if not r1:
            r1 = "Not Applicable"
        s1=request.form.get('Dual_Moniter_SetUp')
        t1=request.form.get('Internet_availability')
        u1=request.form.get('Head_Phone_availability')
        v1=request.form.get('Additional_Key_Board')
        w1=request.form.get('Mouse')
        x1=request.form.get('UPS')
        y1=request.form.get('Proper_Table_availability')
        z1=request.form.get('Proper_Chair_availability')
        a2=request.form.get('Spike_Buster')

        try:  
            with sqlite3.connect("asset.db") as con:
                print("Connected")    
                cur = con.cursor()  
                print("Got cursor")  
                cur.execute("INSERT into details (GID, Emp_Name, Band, CCName, CCID, DOJ, W_Email, Manager, Band_Change_Date, Lead, AGM_VP, Job_Role, T_Name, SPOC, Core_Process, Sub_process, Higher_Qualification, GENDER, DOB, Work_Location, P_Team, Vaccine_Action_Plan, Vaccinated_Status, Vaccination_Certificate_Uploaded, Accomodation, Personal_Email, Insurance, ECName, ECNumber, Mob, Marital, Transport, Distance, Pickup, Address, City_Pin, Native_District, Native_State, Type_of_Asset, CPU_Laptop, Docking_Station, Monitor_1, Monitor_2, Desk_No, Dual_Moniter_SetUp, Internet_availability, Head_Phone_availability, Additional_Key_Board, Mouse, UPS, Proper_Table_availability, Proper_Chair_availability, Spike_Buster) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1,q1,r1,s1,t1,u1,v1,w1,x1,y1,z1,a2))  
                print("executed successfully")  
                con.commit()  
                print("Customer successfully Added")  
                flash("Record Added Successfully","success")
        except Exception as e:   
            con.rollback()
            print(e)  
            print("We can not add the customer to the list" ) 
            flash("Error in Add Record")
        finally:  
            con.close()
            return redirect(url_for('display')) 

@app.route('/test/<gid>', methods=['GET'])
def testfn(gid):
    con = sqlite3.connect("Workday.db")
    cur = con.cursor()  
    cur.execute("select * from Employee_Details where GID = ?",[gid])  
    rows = cur.fetchall()
    return jsonify(rows)  

@app.route('/updateemployee', methods=['POST'])
def updateemployee():
        pk = request.form['pk']
        name = request.form['name']
        value = request.form['value']
        con = sqlite3.connect("asset.db")
        cur = con.cursor()
        if name == 'Emp_Name':
           cur.execute("UPDATE details SET Emp_Name = ? WHERE id = ? ", (value, pk))
        elif name == 'Band':
           cur.execute("UPDATE details SET Band = ? WHERE id = ? ", (value, pk))
        elif name == 'CCName':
           cur.execute("UPDATE details SET CCName = ? WHERE id = ? ", (value, pk))
        elif name == 'CCID':
               cur.execute("UPDATE details SET CCID = ? WHERE id = ? ", (value, pk))
        elif name == 'DOJ':
               cur.execute("UPDATE details SET DOJ = ? WHERE id = ? ", (value, pk))
        elif name == 'W_Email':
               cur.execute("UPDATE details SET W_Email = ? WHERE id = ? ", (value, pk))
        elif name == 'Manager':
               cur.execute("UPDATE details SET Manager = ? WHERE id = ? ", (value, pk))
        elif name == 'Band_Change_date':
               cur.execute("UPDATE details SET Band_Change_date = ? WHERE id = ? ", (value, pk))
        elif name == 'Lead':
               cur.execute("UPDATE details SET Lead = ? WHERE id = ? ", (value, pk))
        elif name == 'AGM_VP':
               cur.execute("UPDATE details SET AGM_VP = ? WHERE id = ? ", (value, pk))
        elif name == 'Job_Role':
               cur.execute("UPDATE details SET Job_Role = ? WHERE id = ? ", (value, pk))
        elif name == 'T_Name':
               cur.execute("UPDATE details SET T_Name = ? WHERE id = ? ", (value, pk))
        elif name == 'SPOC':
               cur.execute("UPDATE details SET SPOC = ? WHERE id = ? ", (value, pk))
        elif name == 'Core_Process':
               cur.execute("UPDATE details SET Core_Process = ? WHERE id = ? ", (value, pk))
        elif name == 'Sub_Process':
               cur.execute("UPDATE details SET Sub_Process = ? WHERE id = ? ", (value, pk))
        elif name == 'Higher_Qualification':
               cur.execute("UPDATE details SET Higher_Qualification = ? WHERE id = ? ", (value, pk))
        elif name == 'GENDER':
               cur.execute("UPDATE details SET GENDER = ? WHERE id = ? ", (value, pk))
        elif name == 'DOB':
               cur.execute("UPDATE details SET DOB = ? WHERE id = ? ", (value, pk))
        elif name == 'Work_Location':
               cur.execute("UPDATE details SET Work_Location = ? WHERE id = ? ", (value, pk))
        elif name == 'P_Team':
               cur.execute("UPDATE details SET P_Team = ? WHERE id = ? ", (value, pk))
        elif name == 'P_O_Team':
               cur.execute("UPDATE details SET P_O_Team = ? WHERE id = ? ", (value, pk))
        elif name == 'Vaccine_Action_Plan':
               cur.execute("UPDATE details SET Vaccine_Action_Plan = ? WHERE id = ? ", (value, pk))
        elif name == 'Vaccinated_Status':
               cur.execute("UPDATE details SET Vaccinated_Status = ? WHERE id = ? ", (value, pk))
        elif name == 'Vaccination_Certificate_Uploaded':
               cur.execute("UPDATE details SET Vaccination_Certificate_Uploaded = ? WHERE id = ? ", (value, pk))
        elif name == 'Accomodation':
               cur.execute("UPDATE details SET Accomodation = ? WHERE id = ? ", (value, pk))
        elif name == 'Personal_Email':
               cur.execute("UPDATE details SET Personal_Email = ? WHERE id = ? ", (value, pk))
        elif name == 'Insurance':
               cur.execute("UPDATE details SET Insurance = ? WHERE id = ? ", (value, pk))
        elif name == 'ECName':
               cur.execute("UPDATE details SET ECName = ? WHERE id = ? ", (value, pk))
        elif name == 'ECNumber':
               cur.execute("UPDATE details SET ECNumber = ? WHERE id = ? ", (value, pk))
        elif name == 'Mob':
               cur.execute("UPDATE details SET Mob = ? WHERE id = ? ", (value, pk))
        elif name == 'Marital':
               cur.execute("UPDATE details SET Marital = ? WHERE id = ? ", (value, pk))
        elif name == 'Transport':
               cur.execute("UPDATE details SET Transport = ? WHERE id = ? ", (value, pk))
        elif name == 'Pickup':
               cur.execute("UPDATE details SET Pickup = ? WHERE id = ? ", (value, pk))
        elif name == 'Distance':
               cur.execute("UPDATE details SET Distance = ? WHERE id = ? ", (value, pk))
        elif name == 'Address':
               cur.execute("UPDATE details SET Address = ? WHERE id = ? ", (value, pk))
        elif name == 'Native_State':
               cur.execute("UPDATE details SET Native_State = ? WHERE id = ? ", (value, pk))
        elif name == 'Native_District':
               cur.execute("UPDATE details SET Native_District = ? WHERE id = ? ", (value, pk))
        elif name == 'City_Pin':
               cur.execute("UPDATE details SET City_Pin = ? WHERE id = ? ", (value, pk))
        elif name == 'Type_of_Asset':
               cur.execute("UPDATE details SET Type_of_Asset = ? WHERE id = ? ", (value, pk))
        elif name == 'CPU_Laptop':
               cur.execute("UPDATE details SET CPU_Laptop = ? WHERE id = ? ", (value, pk))
        elif name == 'Docking_Station':
               cur.execute("UPDATE details SET Docking_Station = ? WHERE id = ? ", (value, pk))
        elif name == 'Monitor_1':
               cur.execute("UPDATE details SET Monitor_1 = ? WHERE id = ? ", (value, pk))
        elif name == 'Monitor_2':
               cur.execute("UPDATE details SET Monitor_2 = ? WHERE id = ? ", (value, pk))
        elif name == 'Desk_No':
               cur.execute("UPDATE details SET Desk_No = ? WHERE id = ? ", (value, pk))
        elif name == 'Dual_Moniter_SetUp':
               cur.execute("UPDATE details SET Dual_Moniter_SetUp = ? WHERE id = ? ", (value, pk))
        elif name == 'Internet_availability':
               cur.execute("UPDATE details SET Internet_availability = ? WHERE id = ? ", (value, pk))
        elif name == 'Head_Phone_availability':
               cur.execute("UPDATE details SET Head_Phone_availability = ? WHERE id = ? ", (value, pk))
        elif name == 'Additional_Key_Board':
               cur.execute("UPDATE details SET Additional_Key_Board = ? WHERE id = ? ", (value, pk))
        elif name == 'Mouse':
               cur.execute("UPDATE details SET Mouse = ? WHERE id = ? ", (value, pk))
        elif name == 'UPS':
               cur.execute("UPDATE details SET UPS = ? WHERE id = ? ", (value, pk))
        elif name == 'Proper_Table_availability':
               cur.execute("UPDATE details SET Proper_Table_availability = ? WHERE id = ? ", (value, pk))
        elif name == 'Proper_Chair_availability':
               cur.execute("UPDATE details SET Proper_Chair_availability = ? WHERE id = ? ", (value, pk))    
        elif name == 'Spike_Buster':
               cur.execute("UPDATE details SET Spike_Buster = ? WHERE id = ? ", (value, pk))
        con.commit()
        cur.close()
        return json.dumps({'status':'OK'})
             
if __name__ == '__main__':
    app.run(debug=True)