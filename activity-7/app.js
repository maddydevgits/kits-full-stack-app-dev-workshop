// it has to get records from db

const express=require('express')
const mysql=require('mysql2')
const url=require('url')

var app=express()

let con=mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'2022Root',
    database:'maddy'
})

app.get('/insertRecordsFromNode',function(request,response){
    let urlData=url.parse(request.url,true);
    let name=urlData.query.name;
    let rollno=urlData.query.rollno;
    let password=urlData.query.password;
    console.log(name,rollno,password)

    con.connect(function(err){
        if(err){
            throw err;
        }
        console.log('connected with db')
        let sql="INSERT INTO fullstack (rollno,name,password) VALUES('"+rollno+"','"+name+"','"+password+"')"
        console.log(sql)
        con.query(sql,function(err,result){
            if(err) {
                throw err;
            }
            response.send('Stored in db');
        })
    })
})

app.get('/getRecordsFromNode',function(request,response){

    con.connect(function(err){
        if(err) {
            throw err;
        }
        console.log('connected with db')
        let sql='select * from fullstack'
        con.query(sql,function(err,result){
            if(err){
                throw err;
            }
            var data=[]
            for (let item of result){
                data.push(JSON.stringify(item))
            }
            response.send(data);
        })
    })
})

app.listen(2000,function(){
    console.log('server started')
})