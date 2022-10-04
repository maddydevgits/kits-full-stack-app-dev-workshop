# API to fetch records from the database

from flask import Flask,request
import mysql.connector as mysql
import json

app=Flask(__name__)
db=mysql.connect(
    host='localhost',
    user='root',
    password='2022Root',
    database='maddy'
)

cur=db.cursor()
app.secret_key='makeskilled'

@app.route('/getRecords',methods=['POST','GET'])
def getRecords():
    sql='select * from fullstack'
    cur.execute(sql)
    result=cur.fetchall()
    data=[]
    for i in result:
        data.append(i)
    return (json.dumps(data))

if __name__=="__main__":
    app.run(debug=True)
