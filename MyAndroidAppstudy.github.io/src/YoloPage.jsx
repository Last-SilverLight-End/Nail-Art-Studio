
import axios from "axios";
import React, { useState, useRef, useEffect, isValidElement } from "react";

import "./App.css";
import loadingYoloImages from "./KakaoTalk_20211129_161520094.jpg";
import $ from "jquery";
const readUrl = (input) => {

    console.log(input);
}

const YoloPage = () => {

    const [yolo_Images, setyolo_Images] = useState(loadingYoloImages);
    const [InputImage, setInputImage] = useState('');

    const [input,setinput] = useState("");
    const [bytestring,setbytestring] = useState('');
    const [image,setimage] = useState('');
    const [file, setFile] = useState("");


    const handleInputChange = (e) => {

        console.log(e.target.files[0]);

       // console.log(e.target.files) // 이걸로 먼저 들어온 파일 리스트 인식
        //console.log(e.target.files[0]); // 파일 안의 내용 인식
        
		setFile(URL.createObjectURL(e.target.files[0]));
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
                <img src={file} />
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