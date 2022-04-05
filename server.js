const express = require('express');
const app = express();
const multer = require("multer");
const path = require("path");
const PORT = 4000;
 
 
app.get('/data',(req,res)=>{
    const data = {
        lastname : "Lee",
        firstname : "chang_Geun"
    };
    res.json(data);
})
 
app.listen(PORT,()=>{
    console.log(`server running on PORT ${PORT}`);
});
