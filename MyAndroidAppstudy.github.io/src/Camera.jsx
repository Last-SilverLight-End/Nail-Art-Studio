import React, { useState, useRef, useEffect } from "react";
import { Camera } from "react-camera-pro";
import * as cocossd from "@tensorflow-models/coco-ssd";
import "./App.css";
import axios from 'axios';
import { time } from "@tensorflow/tfjs";
import { Navigate, useNavigate } from "react-router";
import Loading from './Loading';

const Component = () => {

  const camera = useRef(null);
  const [numberOfCameras, setNumberOfCameras] = useState(0);
  const [selectedFile, setSelectedFile] = useState('');
  const [image, setImage] = useState(null);
  const navigate = useNavigate();
  // const [isLoading,setIsLoading] = useState<Boolean>(false);
  const todayTime = () => {
    let now = new Date().toString();
    return now;
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
  const  submit = () => {
    //바꾼 파일을 

    const convertedFile = dataURLtoFile(image, todayTime() + ".png");
    const data = new FormData();
    data.append('file', convertedFile);
    console.warn(convertedFile);
    
    let url = "/uploader";


    /* axios.post(url, data, {
        // 주소와 formdata를 posting 한다
     })
     .then(res => { 
       //상태 출력
         console.warn(res);
     });*/


    setTimeout(() => {
      navigate('/SelectPage');
    }, 3000);

  }

  return (
    <div>
      <Camera ref={camera}
        numberOfCamerasCallback={setNumberOfCameras}
        aspectRatio={16 / 9}
        facingMode='environment'
      />

      <img src={image} alt='이미지 미리보기'

      />
      <button
        onClick={() => {
          const photo = camera.current.takePhoto();
          setImage(photo);
        }}
      > 카메라 사진 찍기</button>
      <button
        hidden={numberOfCameras <= 1}
        onClick={() => {
          camera.current.switchCamera();
        }}
      >카메라 전환 </button>
      <button type="submit"
        onClick={() => submit()}> 업로드 하기</button>
    </div>
  );
}

export default Component;