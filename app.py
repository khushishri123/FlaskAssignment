from flask import *
import sqlite3

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")

    

@app.route("/saveDetails",methods=['POST'])
def saveDetails():
    msg=""
    try:  
            name = request.form["name"]  
            percentage = request.form["percentage"]  
            with sqlite3.connect("student.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Student (name, percentage) values (?,?)",(name,percentage))  
                con.commit()  
                msg = "Student successfully Added"  
    except:  
            con.rollback()  
            msg = "We can not add the student to the list"  
    finally:  
            return render_template("success.html",msg = msg)  
            con.close()  
            
        
#View Students list
@app.route("/viewStudents",methods=['GET','POST'])  
def viewStudents():  
    con = sqlite3.connect("student.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Student")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)   



#Delete module
@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods=['POST','GET'])
def deleteRecord():
    msg=""
    try:
        roll_no=request.form['roll_no']
        with sqlite3.connect("student.db") as con:
            cur=con.cursor()
            cur.execute("delete from Student where roll_no=?",roll_no)
            con.commit()
            msg="Student deleted successfully"
    except:
        con.rollback()
        msg="Unable to delete student"
    finally:
        return render_template("deleterecord.html",msg=msg)
        con.close()

#update Student
@app.route("/update")
def update():
    return render_template("updateForm.html")


@app.route('/confirmUpdateRecord',methods=['POST','GET'])  
def ConfirmUpdateRecord():
    roll_no=request.form['roll_no']
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    query="select * from Student where roll_no=?"
    result=cur.execute(query,(roll_no))  
    row=result.fetchone()
    if row:
        return render_template('confirmUpdateForm.html',row=row)

@app.route("/updateRecord",methods=['GET','POST'])
def updateRecord():
    roll_no=request.form['roll_no']
    name=request.form['name']
    percentage=request.form['percentage']
    msg=""
    try:
        with sqlite3.connect("student.db") as con:
          cur=con.cursor()
          cur.execute("update Student set name=?,percentage=? where roll_no=?",(name,percentage,roll_no))
          con.commit()
          msg="Student Data updated successfully"
    except:
        con.rollback()
        msg="Unable to update data"
    finally:
        con.close()
        return render_template("updateRecord.html",msg=msg)          





   
if __name__=="__main__":
    app.run(debug=True)