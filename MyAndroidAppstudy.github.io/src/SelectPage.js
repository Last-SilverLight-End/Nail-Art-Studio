import React, { useState, useRef, useEffect } from "react";
import { Camera } from "react-camera-pro";
import * as cocossd from "@tensorflow-models/coco-ssd";
import "./App.css";
import axios from 'axios';
import { time } from "@tensorflow/tfjs";
import { Navigate, useNavigate } from "react-router";


const ZepetoAuto = () => {
    
}

const SelectPage = () => {
    const [image, setShowImage] = useState('');


    return (
        <div className="App-header">
            <h1 > 사진 미리보기 </h1>
            <img src="08c3d43117adf478.jpg" ></img>
            <h1>Zepeto</h1>
            <button className="buttonshow" onClick={() =>
                window.open('https://studio.zepeto.me/kr/console/auth/signin', '_blank')}>
                Zepeto로 안내</button>
            <h1>SnapChat</h1>
                <button className="buttonshow" onClick={() =>
                window.open('https://accounts.snapchat.com/accounts/login?continue=%2Faccounts%2Fwelcome', '_blank')}>
                snapchat으로 안내</button>


        </div>
    );
};

export default SelectPage;