
import { setPlatform } from "@tensorflow/tfjs";
import axios from "axios";
import React, { useState, useRef, useEffect, isValidElement } from "react";

import "./App.css";
import loadingYoloImages from "./KakaoTalk_20211129_161520094.jpg";
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

    const [input,setinput] = useState("");
    const [bytestring,setbytestring] = useState('');
    const [image,setimage] = useState('');
    const [file, setFile] = useState(dataURLtoFile(sessionStorage.getItem("image"), "anonymous.png"));
    const [previewfile, setPreviewFile] = useState(sessionStorage.getItem("image"));

    const handleInputChange = (e) => {

        console.log(e.target.files[0]);

       // console.log(e.target.files) // 이걸로 먼저 들어온 파일 리스트 인식
        //console.log(e.target.files[0]); // 파일 안의 내용 인식
        
		setPreviewFile(URL.createObjectURL(e.target.files[0]));
        setFile(e.target.files[0]);
        console.log(file);

       
    };

    const upLoad = async () => {
        //console.log(file);
        const formData = new FormData();
        formData.append('file',file)
        let url = "http://localhost:5000/detectObject";
        axios.post(url,formData,{
        }).then(res => {
            console.log(res);
            const bytestring = res.data.status.split('\'')[1];
            setPreviewFile(`data:image/jpeg;base64,${bytestring}`);
        }).catch(err => {
            console.log("upload error" , err);
        })
    }


    return (
        <div className='App'>
            <header className='App-header'>
                <p>
                    Object Detection - YOLO
                </p>

                <div className="pre_img">
                <img src={previewfile} />
                </div>

                <form>
                    <input id="imageinput" type="file" name="image" onChange={ handleInputChange }  />
                </form>
                <button name="send" id="sendbutton" onClick = {() => upLoad()}>Send</button>
            </header>
        </div>
    );
}



export default YoloPage;