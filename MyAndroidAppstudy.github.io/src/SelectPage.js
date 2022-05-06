import React, { useState, useRef, useEffect } from "react";
import { Camera } from "react-camera-pro";
import * as cocossd from "@tensorflow-models/coco-ssd";
import "./App.css";
import axios from 'axios';
import { time } from "@tensorflow/tfjs";
import { Navigate, useNavigate } from "react-router";




const SelectPage = () => {
    const [image, setShowImage] = useState('');


    return( 
         <div>
             사진 미리보기
            <img  src = "08c3d43117adf478.jpg" ></img>
            
             <button onClick = {() => window.open('https://studio.zepeto.me/kr/console/auth/signin', '_blank')}>Zepeto로 안내</button>

             <h1>snap chat으로 안내</h1>
             
        </div>
    );
};

export default SelectPage;