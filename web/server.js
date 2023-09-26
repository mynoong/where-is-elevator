const express = require('express');
const app = express();

const MongoClient = require('mongodb').MongoClient;

var db;
MongoClient.connect('mongodb+srv://gogetterminwoong:mw0326peter7@clustermw.vmgrpeo.mongodb.net/?retryWrites=true&w=majority', function(error, client){
    if (error) return console.log(error)

    db = client.db('elevator');

    db.collection('number').insertOne({이름 : 'John', 나이 : 20}, function(error, result){
        console.log('저장완료');
    });

    app.listen(8080, function(){
        console.log('listening on 8080')
    });
});

app.get('/pet', function(req, res){
    res.send('펫쇼핑할 수 있는 사이트입니다.');
});

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
});