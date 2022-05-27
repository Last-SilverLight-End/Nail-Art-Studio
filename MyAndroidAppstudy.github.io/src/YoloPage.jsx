import { input } from "@tensorflow/tfjs";
import axios from "axios";
import React, { useState, useRef, useEffect } from "react";

import "./App.css";
import loadingYoloImages from "./KakaoTalk_20211129_161520094.jpg";


const readUrl = (item) => {

    console.log("started readUrl");

    if (item.files && item.files[0]) {
        let formData = new FormData();
        formData.append('images', input.files[0]);

        let url = "/detectObject";
        axios({
            method: 'POST',
            url: url,
            data: formData,
            headers: {
                'cache': false,
                'processData': false,
                'Content-Type': false,
            },
        }).then((response) => {
            console.log("response", response);
            bytestring = (data['status']);
            image = bytestring.split('\'')[1]
            imagebox.attr('src', 'data:image/jpeg;base64,' + image)

        }).catch(function (error) {
            console.log(error);
        });
    }

    const YoloPage = () => {

        const [yolo_Images, setyolo_Images] = useState(loadingYoloImages);
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
}


export default YoloPage;