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
    const [previewfile, setPreviewFile] = useState(sessionStorage.getItem("image"));
    const [previewfile2, setPreviewFile2] = useState(sessionStorage.getItem("image"));
    const [gotonextcheck, setGoToNextCheck] = useState(true);
    const [savebase64data, setSaveBase64Data] = useState("");
    const [rotate, setRotate] = useState([0, 0, 0, 0, 0]);
    const [rotateleft, setRotateleft] = useState(0);
    const handleInputChange = async (e) => {

        console.log(e.target.files[0]);

        // console.log(e.target.files) // 이걸로 먼저 들어온 파일 리스트 인식
        //console.log(e.target.files[0]); // 파일 안의 내용 인식

        setPreviewFile(URL.createObjectURL(e.target.files[0]));
        setFile(e.target.files[0]);
        setPreviewFile2(URL.createObjectURL(e.target.files[0]));
        setFile2(e.target.files[0]);
        console.log(file);
        console.log(file2);

        const reader = new FileReader();
        reader.readAsDataURL(e.target.files[0]);
        reader.onloadend = () => {
            const base64data = reader.result;
            console.log(base64data);
            setSaveBase64Data(base64data);
        }



    };

    

    const Submit = async () => {
        for (let i = 0; i < 5; i++) {
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
                ctx.drawImage(image_temp, -canvas.width / 2, -canvas.height / 2, canvas.width, canvas.height);
                ctx.restore();
            }
            console.log(canvas.toDataURL());

            const formData = new FormData();
            let name = "finger" + i;
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
                }
                else {
                    console.log("good")
                }

            }).catch(err => {
                console.log("upload error", err);
            })
        }

    }

    const gotoNext = async () => {
        //console.log(file);

        const formData = new FormData();
        formData.append('file', file2);
        let route = file2.name;
        console.log(route);
        formData.append('route', route);
        let url = "/cropping"

        /* axios.post(url,formData,{
         }).then(res => {
             console.log(res.data);
             if(res.data == "error occured")
             {
                 console.log("not good")
                 setGoToNextCheck(false);
                 setPreviewFile(loadingYoloImages);
             }
 
             else{
                 console.log("good")
                 setGoToNextCheck(true);
             }
            
             
         
         }).catch(err => {
             console.log("upload error" , err);
             setNext(false);
         })*/

        setTimeout(() => {


            if (typeof window !== "undefined") {
                console.log("gogo");
                console.log(gotonextcheck);
                if (gotonextcheck == true) {
                    window.sessionStorage.setItem("image_yolo3", previewfile);
                    window.location.href = "/SelectPage";
                    // crop 과 merge 해서 보여주는 코드
                    // setPreviewFile("http://localhost:5000/bringimg")
                    //setPreviewFile(require("./../image/nft_image.png"))  
                }
                else {
                    alert("이미지가 좋지 않습니다 다른 이미지로 시도해 주세요!")
                }
            }
        }, 3000);

    }

    const Rotating_Left = (i) => {
        rotate[i]--;
        setRotate([...rotate]); // call by reference setRotate(rotate)로 하면 안됨
    }

    const Rotating_Right = (i) => {
        rotate[i]++;
        setRotate([...rotate]);
    }

    const previewFiles = [previewfile, previewfile2, previewfile, previewfile, previewfile];

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
                        <button className="rotatebuttonLeft" onClick={() => { Rotating_Left(i) }}>돌리기</button>
                        <button className="rotatebuttonRight" onClick={() => { Rotating_Right(i) }}>돌리기</button>
                    </div>)}
                </div>

                <div>
                    <button className=" submit " onClick={() => { Submit() }}> 저장하기</button>
                </div>


                {/* <button name="send" id="sendbutton" onClick={() => upLoad()}>Send</button> */}
                {/*  <button name="send2" id="sendbutton2" onClick = {() => upLoad2()}>Send2</button> */}
                <button name="next" id="gotonext" onClick={() => gotoNext()}>go to Next</button>
            </header>
        </div>
    );
}



export default YoloPage;
