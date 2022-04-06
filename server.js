const express = require('express');
const app = express();
const multer = require("multer");
const path = require("path");
const PORT = 5000;
const router = express.Router();
const upload = multer({ dest: 'uploads/' })

app.use(express.static("public"));

const storage = multer.diskStorage({
   destination : "./uploads",
    filename: function(req, file, cb)  {
        cb(null, "imgfile" + Date.now() + path.extname(file.originalname));
    },
    }
);

 upload = multer({ storage: storage, limits: {fileSize : 1000000} }).single("profile_img");

app.post("/profile", upload.array("img",12), function(req, res, next) {
    res.send({
      fileName: req.file.filename
    });
  });

app.get('/data',(req,res)=>{
    const data = {
        lastname : "Lee",
        firstname : "chang_eGeun"
    };
    res.json(data);
})
 
app.listen(PORT,()=>{
    console.log(`server running on PORT ${PORT}`);
});




app.post("/upload", upload.single("img"), function(req, res, next) {
    res.send({
      fileName: req.file.filename
    });
  });
