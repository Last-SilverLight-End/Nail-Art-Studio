import axios from "axios";
import React, { useState, useRef, useEffect } from "react";

import "./App.css";
import loadingYoloImages from "./KakaoTalk_20211129_161520094.jpg";
import $ from "jquery";

const YoloPage = () => {

    const [yolo_Images, setyolo_Images] = useState(loadingYoloImages);
    const [InputImage, setInputImage] = useState('');
    const [imagebox,setimagebox] = useState('');
    const [input,setinput] = useState('');
    const [bytestring,setbytestring] = useState('');
    const [image,setimage] = useState('');
    const handleChangeFile = (evt) => {

        if (evt.target.files.length) {
            let imgTarget = (evt.target.files)[0];
            let fileReader = new FileReader();
            setInputImage(imgTarget);
            fileReader.readAsDataURL(imgTarget);
            fileReader.onload = function (e) {
                /* file을 꺼내서 State로 지정 */
                setyolo_Images(e.target.result);
            }
        }
    }


    return (
        <div class='App'>
            <header class='App-header'>
                <p><u>
                    Object Detection - YOLO
                </u></p>
                <div className="pre_img">
                    <span><img id="imagebox" src="" /></span>
                </div>
                <form>
                    <input id="imageinput" type="file" name="image"  />
                </form>
                <button name="send" id="sendbutton">Send</button>
            </header>
        </div>
    )
};


export default YoloPage;