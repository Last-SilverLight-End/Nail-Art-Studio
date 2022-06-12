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
    const [next, setNext] = useState(false);
    const [input, setinput] = useState("");
    const [bytestring, setbytestring] = useState('');
    const [image, setimage] = useState('');
    const [file, setFile] = useState(dataURLtoFile(sessionStorage.getItem("image"), "anonymous.png"));
    const [file2, setFile2] = useState(dataURLtoFile(sessionStorage.getItem("image"), "anonymous.png"));
    const [previewfile0, setPreviewFile0] = useState("http://localhost:5000/bringimg2/Thumb.png");
    const [previewfile1, setPreviewFile1] = useState("http://localhost:5000/bringimg2/Index.png");
    const [previewfile2, setPreviewFile2] = useState("http://localhost:5000/bringimg2/Middle.png");
    const [previewfile3, setPreviewFile3] = useState("http://localhost:5000/bringimg2/Ring.png");
    const [previewfile4, setPreviewFile4] = useState("http://localhost:5000/bringimg2/Pinky.png");
    const [savebase64data, setSaveBase64Data] = useState("");
    const [rotate, setRotate] = useState([0, 0, 0, 0, 0]);
    const [rotateleft, setRotateleft] = useState(0);



    const previewFiles = [previewfile0, previewfile1, previewfile2, previewfile3, previewfile4];


    const Submit = async () => {
        const finger_name = ["Thumb","Index","Middle","Pinky","Ring"]
        
        for (let i = 0; i < 5; i++) {

            const image_temp2 = document.createElement("img")
            image_temp2.src = previewFiles[i];
            image_temp2.crossOrigin = 'anonymous';
            image_temp2.onload = () => {
                const canvas = document.createElement("canvas");

                canvas.width = 200;
                canvas.height = 200;
                let image_temp = document.getElementById(`image${i}`);

                let ctx = canvas.getContext("2d");
                drawRotated(rotate[i])
                function drawRotated(degrees) {

                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                    ctx.save();
                    ctx.translate(canvas.width / 2, canvas.height / 2);
                    ctx.rotate(degrees * Math.PI / 180);
                    ctx.drawImage(image_temp2, -canvas.width / 2, -canvas.height / 2, canvas.width, canvas.height);
                    ctx.restore();

                } 
                console.log(canvas.toDataURL());

                const formData = new FormData();
                let name = finger_name[i];
                const convertedFile = dataURLtoFile(canvas.toDataURL(), name + ".png");

                console.warn(convertedFile)
                formData.append('file', convertedFile)
                formData.append('name', name);

                let url = "/uploader2";
                axios.post(url, formData, {
                }).then(res => {
                    console.log(res.data);
                    if (res.data == "error occured") {
                        console.log("not good")
                        console.log(res.data)
                    }
                    else {
                        console.log("good")
                        console.log(res.data)
                    }

                }).catch(err => {
                    console.log("upload error", err);
                })
                let url2 = "/cropping2"
                axios.get(url2,{
                }).then(res => {
                    console.log(res.data);
                    if(res.data == "error occured")
                    {
                        console.log("not good")
                       
                    }
                    else{
                        console.log("good")
                        
                    }
                   
                
                }).catch(err => {
                    console.log("upload error" , err);
                    
                })
            }

            //window.location.href = "/SelectPage";


        }

    /*    let url2 = "/uploading"
        const formData2 = new FormData();
        formData2.append('route')
        axios.post(ulr2,formData2{

        }).*/

    }

    const Rotating_Left = (i) => {
        rotate[i]--;
        setRotate([...rotate]); // call by reference setRotate(rotate)로 하면 안됨
    }

    const Rotating_Right = (i) => {
        rotate[i]++;
        setRotate([...rotate]);
    }

    //let a = [];

    //a[0] = 1;   // a = [ 1 ];
    //a.push(2); // // a = [ 1, 2 ];
    //a[1]++;     // a = [ 1, 3 ];

    return (
        <div className='App'>
            <header className='App-header'>
                <p>
                    손가락 돌려보세요! 
                </p>

                <div className="pre_img" style={{ display: 'flex' }}>
                    {Array(5).fill().map((_, i) => <div key={i}>
                        <div style={{ overflow: "hidden" }}>
                            <img id={`image${i}`} className="showRotateImage" src={previewFiles[i]}
                                style={{ transform: `rotate(${rotate[i]}deg)` }} />
                        </div>
                        <br />
                        <button className="rotatebuttonLeft" onClick={() => { Rotating_Left(i) }}>Right</button>
                        <button className="rotatebuttonRight" onClick={() => { Rotating_Right(i) }}>Left</button>
                    </div>)}
                </div>

                <div>
                    <button className="rotatebuttonLeft" Name=" submit "  onClick={() => { Submit() }}> 저장하기</button>
                </div>


                {/* <button name="send" id="sendbutton" onClick={() => upLoad()}>Send</button> */}
                {/*  <button name="send2" id="sendbutton2" onClick = {() => upLoad2()}>Send2</button> */}

            </header>
        </div>
    );
}



export default YoloPage;