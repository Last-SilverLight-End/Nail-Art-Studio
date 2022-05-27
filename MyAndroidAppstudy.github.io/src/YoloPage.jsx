
import axios from "axios";
import React, { useState, useRef, useEffect, isValidElement } from "react";

import "./App.css";
import loadingYoloImages from "./KakaoTalk_20211129_161520094.jpg";

const readUrl = (input) => {

    console.log(input);
}

const YoloPage = () => {

    const [yolo_Images, setyolo_Images] = useState(loadingYoloImages);
    const [InputImage, setInputImage] = useState('');
    const [imagebox,setimagebox] = useState('');
    const [input,setinput] = useState("");
    const [bytestring,setbytestring] = useState('');
    const [image,setimage] = useState('');
    const [file, setFile] = useState(null);


    const handleInputChange = (e) => {
        if(e.files && e.files[0]){
            let reader = new FileReader();
            reader.onload = function(e){
                console.log(e)

                
            }
            reader.readAsDataURL(e.files[0]);
            setFile(e.target.files[0]);
        }
       
    };

        



    return (
        <div className='App'>
            <header className='App-header'>
                <p><u>
                    Object Detection - YOLO
                </u></p>
                <div className="pre_img">
                    <span><img id="imagebox" src="" /></span>
                </div>
                <form>
                    <input id="imageinput" type="file" name="image" onChange={handleInputChange}  />
                </form>
                <button name="send" id="sendbutton">Send</button>
            </header>
        </div>
    );
}



export default YoloPage;