import React, { useState, useRef, useEffect } from "react";
import { Camera } from "react-camera-pro";
import "./App.css";
import axios from 'axios';
//import * as tf from "@tensorflow/tfjs";
import { Navigate, useNavigate } from "react-router";
import * as tmImage from '@teachablemachine/image';
//import { model } from "@tensorflow/tfjs";
import Resizer from "react-image-file-resizer";
const Component = () => {

  const camera = useRef(null);
  const [numberOfCameras, setNumberOfCameras] = useState(0);
  const [selectedFile, setSelectedFile] = useState('');
  const [image, setImage] = useState(null);
  const navigate = useNavigate();
  const [showResult,setShowResult]=useState(false);
  //const [photo,setPhoto] = useState('');
  // const [isLoading,setIsLoading] = useState<Boolean>(false);

  // teachable machine 모텔 불러오기 코드
  const URL = "https://teachablemachine.withgoogle.com/models/Ab3ndS3RI/";
  const modelURL = URL + "model.json";
  const metadataURL = URL + "metadata.json";
  const [predictionArr,setPredictionArr]=useState([]);
  let maxPredictions;
  let model;
  //현재 시간
  const todayTime = () => {
    let now = new Date().toString();
    return now;
  }
  // 이미지 resize

  const resizeFile = (file) =>
  new Promise((resolve) => {
    Resizer.imageFileResizer(
      file,
      244,
      244,
      "PNG",
      122,
      0,
      (uri) => {
        resolve(uri);
      },
      "base64"
    );
  });

  
  async function init () {
    model = await tmImage.load(modelURL,metadataURL);
    maxPredictions = model.getTotalClasses();

  }



  const handleChangeFile = (e) => {

  }
  async function predict () {


    model = await tmImage.load(modelURL,metadataURL);
    maxPredictions = model.getTotalClasses();


    //const tempImage = document.getElementById('srcImg');
    
    
   // const convertedFile = dataURLtoFile(image, todayTime() + ".png");
    //const prediction = await model.predict(convertedFile);
   // console.log(prediction[0].probability);
    //setPredictionArr(prediction)
    //setShowResult(true)
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

  const  submit = async() => {

    // 먼저 파일 변환 후에 
    const convertedFile = dataURLtoFile(image, todayTime() + ".png");
    console.warn(convertedFile);

    //파일 사이즈 조절
    const file = convertedFile;
    const imagetemp = await resizeFile(file);
    console.log(imagetemp);
    const newFile = dataURLtoFile(imagetemp, todayTime() + ".png");


    // 그다음 데이터 형식으로 만들어서 파일로 서버한테 전송 시킨다.
    const data = new FormData();
    data.append('file', newFile);
    console.warn(newFile);
    
    let url = "/uploader";


     axios.post(url, data, {
        // 주소와 formdata를 posting 한다
     })
     .then(res => { 
       //상태 출력
         console.warn(res);
     });


    setTimeout(() => {
      //navigate('/Loading');
    }, 10000);

  }

  return (
    <div>
      <Camera ref={camera}
        numberOfCamerasCallback={setNumberOfCameras}
        aspectRatio={16 / 9}
        facingMode='environment'
      />
      <img id = "srcimg" className="image-size" src={image} alt='이미지 미리보기'

      />
      <button
        onClick={() => {
          const photo = (camera.current.takePhoto());
          setImage(photo);
         /* predict();*/
          
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