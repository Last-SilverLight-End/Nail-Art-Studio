import React, { useState, useRef, useEffect } from "react";

import "./App.css";
import loadingYoloImages from "./KakaoTalk_20211129_161520094.jpg";

const YoloPage = () => {

    const [yolo_Images,setyolo_Images] = useState(loadingYoloImages);
    return (
        <div class='App'>
            <header class='App-header'>
                <p><u>
                    Object Detection - YOLO
                </u></p>
                <div className="pre_img">
                    <span><img id="imagebox" src={yolo_Images} /></span>
                </div>
                <form>
                    <input id="imageinput" type="file" name="image" onchange="readUrl(this)" />
                </form>
                <button name="send" id="sendbutton">Send</button>
            </header>
        </div>
    )
};


export default YoloPage;