from flask import Flask, render_template,request,session,redirect
import mysql.connector as mysql

db=mysql.connect(
    host='localhost',
    user='root',
    password='2022Root',
    database='maddy'
)

cur=db.cursor()

app=Flask(__name__)
app.secret_key='makeskilled'

@app.route('/')
def indexPage():
    return render_template('register.html')

@app.route('/collect',methods=['POST'])
def collectFromRegister():
    name=request.form['name']
    rollno=request.form['rollno']
    password=request.form['password']
    cur.execute('SELECT rollno FROM fullstack')
    result=cur.fetchall()
    flag=0
    for x in result:
        if(rollno==x[0]):
            flag=1
            return render_template('register.html',result='Existed User')
    if(flag==0):
        sql="INSERT INTO fullstack (rollno,name,password) VALUES (%s,%s,%s)"
        values=(rollno,name,password)
        cur.execute(sql,values)
        db.commit()
        if(cur.rowcount==1):
            return render_template('register.html',result='registered successfully')
        else:
            return render_template('register.html',result='register failed')


@app.route('/loginPage')
def loginPage():
    return render_template('login.html')

@app.route('/logoutPage')
def logoutPage():
    del(session['username'])
    del(session['password'])
    return redirect('/')

@app.route('/dashboard')
def dashboardPage():
    try:
        if session['username'] and session['password']:
            cur.execute('SELECT * FROM fullstack')
            result=cur.fetchall()
            data=[]
            for i in result:
                data.append(i)
            return render_template('dashboard.html',result=data)
    except:
        return render_template('register.html')

@app.route('/loginCollect',methods=['POST'])
def dataFromLoginPage():
    rollno=request.form['rollno']
    password=request.form['password']
    cur.execute('SELECT * FROM fullstack')
    result=cur.fetchall()
    flag=0
    for x in result:
        if(rollno==x[0] and password==x[2]):
            flag=1
            session['username']=rollno
            session['password']=password
            return redirect('/dashboard')
    if(flag==0):
        return render_template('login.html',result='invalid credentials')

if __name__=="__main__":
    app.run(debug=True)