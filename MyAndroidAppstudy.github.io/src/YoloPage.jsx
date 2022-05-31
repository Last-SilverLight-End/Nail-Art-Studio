import { setPlatform } from "@tensorflow/tfjs";
import axios from "axios";
import React, { useState, useRef, useEffect, isValidElement } from "react";

import "./App.css";
import loadingYoloImages from "./slimeimg1.png";
const readUrl = (input) => {

    console.log(input);
}

const dataURLtoFile = (dataurl, fileName) => {

    var arr = dataurl.split(','),
      mime = arr[0].match(/:(.*?);/)[1],
      bstr = atob(arr[1]),
      n = bstr.length,
      u8arr = new Uint8Array(n);

    while (n--) {
      u8arr[n] = bstr.charCodeAt(n);
    }

    return new File([u8arr], fileName, { type: mime });
  }

const YoloPage = () => {

    const [yolo_Images, setyolo_Images] = useState(loadingYoloImages);
    const [InputImage, setInputImage] = useState('');
    const [next,setNext] = useState(false);
    const [input,setinput] = useState("");
    const [bytestring,setbytestring] = useState('');
    const [image,setimage] = useState('');
    const [file, setFile] = useState(dataURLtoFile(sessionStorage.getItem("image"), "anonymous.png"));
    const [file2, setFile2] = useState(dataURLtoFile(sessionStorage.getItem("image"), "anonymous.png"));
    const [previewfile, setPreviewFile] = useState(sessionStorage.getItem("image"));
    const [previewfile2, setPreviewFile2] = useState(sessionStorage.getItem("image"));
    const [gotonextcheck, setGoToNextCheck] = useState(false);
    const handleInputChange = (e) => {

        console.log(e.target.files[0]);

       // console.log(e.target.files) // 이걸로 먼저 들어온 파일 리스트 인식
        //console.log(e.target.files[0]); // 파일 안의 내용 인식
        
		setPreviewFile(URL.createObjectURL(e.target.files[0]));
        setFile(e.target.files[0]);
        setPreviewFile2(URL.createObjectURL(e.target.files[0]));
        setFile2(e.target.files[0]);
        console.log(file);
        console.log(file2);

       
    };

    const upLoad = async () => {
        //console.log(file);
        const formData = new FormData();
        formData.append('file',file)
        let url = "/detectObject";

        function SelectPageClick(e){
            window.location.href = "/SelectPage"
          }
          console.log(previewfile);
          
        axios.post(url,formData,{
        }).then(res => {
            console.log(res.data);
            if(res.data == "error occured")
            {
                console.log("not good")
                setGoToNextCheck(false);
                setPreviewFile(loadingYoloImages)
            }
            else{
                console.log("good")
                setGoToNextCheck(true);
                const bytestring = res.data.status.split('\'')[1];
                setPreviewFile(`data:image/png;base64,${bytestring}`);
                console.log(previewfile);
                setNext(true);
            }
           
            
        
        }).catch(err => {
            console.log("upload error" , err);
            setNext(false);
        })
        /*setTimeout(() => {
            if(typeof window !== "undefined"){
                console.log("gogo");
                if(previewfile == previewfile2)
                {
                    console.log("wtf?");
                }
                //window.sessionStorage.setItem("image_yolo", previewfile);
               // window.location.href = "/SelectPage";
            }
        }, 5000);*/
       // upLoad2();
    }

    const gotoNext = async () => {
        //console.log(file);
        
          
        setTimeout(() => {
            if(typeof window !== "undefined"){
                console.log("gogo");
                
                window.sessionStorage.setItem("image_yolo2", previewfile2);
                window.location.href = "/SelectPage";
            }
        }, 3000);
        
    }

    return (
        <div className='App'>
            <header className='App-header'>
                <p>
                    손이 제대로 인식 되었는지 확인하세요!
                </p>

                <div className="pre_img">
                {gotonextcheck ? <img src={previewfile} /> : <img src = {previewfile2}/>}
               
                </div>

                <form>
                    <input id="imageinput" type="file" name="image" onChange={ handleInputChange }  />
                </form>
                <button name="send" id="sendbutton" onClick = {() => upLoad()}>Send</button>
               {/*  <button name="send2" id="sendbutton2" onClick = {() => upLoad2()}>Send2</button> */}
               <button name = "next" id = "gotonext" onClick = {() => gotoNext()}>go to Next</button>
            </header>
        </div>
    );
}



export default YoloPage;
