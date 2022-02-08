const express = require('express');
const cors = require('cors');
// const mongoose = require('mongoose');
const morgan = require('morgan');
const router = require('./route/hellow'); 
const app = express();
// const viengin = express 
require('dotenv').config();
const port = process.env.PORT || 3001;

// connecting to the database  
// mongoose.connect(process.env.DBURL,{useNewUrlParser:true,useUnifiedTopology:true}).then(()=>{
//     console.log('connections was successfull !!');
// });
// erro
// mongoose.connection.on('error',error => {
//     console.log('db is not connected properly pleace try again !!');
// });
 
// use static files
app.use(express.static(__dirname + '/view'));

app.use(router);
// use module middlewer
app.use(morgan('dev'));
app.use(cors);


// listing url
app.listen(port,()=>{
    console.log(`copy this url -> localhost:${port}`);
});