from flask import Flask,render_template,request,session
import mysql.connector as mysql

db=mysql.connect(
    host='localhost',
    user='root',
    password='2022Root',
    database='maddy'
)

cur=db.cursor()

app=Flask(__name__)
app.secret_key='maddy123'

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/about')
def aboutPage():
    return render_template('about.html',rollno=session['rollno'],name=session['name'])

@app.route('/collect',methods=['POST'])
def collectData():
    r=request.form['rollno']
    n=request.form['name']
    # print(r,n)
    storeData(r,n)
    session['rollno']=r
    session['name']=n

    result='data collected'
    return(render_template('index.html',result=result))


@app.route('/getdata',methods=['GET','POST'])
def getDataFromDB():
    cur.execute("SELECT * FROM fullstack")
    result=cur.fetchall()
    data=[]
    for i in result:
        data.append(i)
    return(str(data))


def storeData(rollno,name):
    sql='INSERT INTO tablename (rollno,name) VALUES (%s,%s)'
    val=(rollno,name)
    cur.execute(sql,val)
    db.commit()

if __name__=="__main__":
    app.run(debug=True)