import React, { useState, useRef, useEffect } from "react";
import { Camera } from "react-camera-pro";
import "./App.css";
import axios from 'axios';
//import * as tf from "@tensorflow/tfjs";
import { Navigate, useNavigate } from "react-router";
import * as tmImage from '@teachablemachine/image';
//import { model } from "@tensorflow/tfjs";
import Resizer from "react-image-file-resizer";

import styled from 'styled-components';

const Control = styled.div`
  position: fixed;
  display: flex;
  right: 0;
  width: 20%;
  min-width: 130px;
  min-height: 130px;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 50px;
  box-sizing: border-box;
  flex-direction: column-reverse;
  @media (max-aspect-ratio: 1/1) {
    flex-direction: row;
    bottom: 0;
    width: 100%;
    height: 20%;
  }
  @media (max-width: 400px) {
    padding: 10px;
  }
`;

const Wrapper = styled.div`
  position: fixed;
  width: 100%;
  height: 100%;
  z-index: 1;
`;
const FullScreenImagePreview = styled.div`
  width: 100%;
  height: 100%;
  z-index: 100;
  position: absolute;
  background-color: black;
  ${({ image }) => (image ? `background-image:  url(${image});` : '')}
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
`;

const ImagePreview = styled.div`
  width: 100px;
  height: 100px;
  ${({ image }) => (image ? `background-image:  url(${image});` : '')}
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  @media (max-width: 400px) {
    width: 50px;
    height: 120px;
  }
`;

const Button = styled.button`
  outline: none;
  color: white;
  opacity: 1;
  background: transparent;
  background-color: transparent;
  background-position-x: 0%;
  background-position-y: 0%;
  background-repeat: repeat;
  background-image: none;
  padding: 0;
  text-shadow: 0px 0px 4px black;
  background-position: center center;
  background-repeat: no-repeat;
  pointer-events: auto;
  cursor: pointer;
  z-index: 2;
  filter: invert(100%);
  border: none;
  &:hover {
    opacity: 0.7;
  }
`;

const TakePhotoButton = styled(Button)`
  background: url('https://img.icons8.com/ios/50/000000/compact-camera.png');
  background-position: center;
  background-size: 50px;
  background-repeat: no-repeat;
  width: 80px;
  height: 80px;
  border: solid 4px black;
  border-radius: 50%;
  &:hover {
    background-color: rgba(0, 0, 0, 0.3);
  }
`;

const ChangeFacingCameraButton = styled(Button)`
  background: url(https://img.icons8.com/ios/50/000000/switch-camera.png);
  background-position: center;
  background-size: 40px;
  background-repeat: no-repeat;
  width: 40px;
  height: 40px;
  padding: 40px;
  &:disabled {
    opacity: 0;
    cursor: default;
    padding: 60px;
  }
  @media (max-width: 400px) {
    padding: 40px 5px;
    &:disabled {
      padding: 40px 25px;
    }
  }
`;





const Component = () => {

  const camera = useRef(null);
  const [numberOfCameras, setNumberOfCameras] = useState(0);
  const [selectedFile, setSelectedFile] = useState('');
  const [image, setImage] = useState(null);
  const navigate = useNavigate();
  const [showResult,setShowResult]=useState(false);
  const [showImage, setShowImage] = useState(false);
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
    <Wrapper>
      {showImage ? (
        <FullScreenImagePreview
          image={image}
          onClick={() => {
            setShowImage(!showImage);
          }}
          />
      )
      :(
      <Camera ref={camera}
        numberOfCamerasCallback={setNumberOfCameras}
        aspectRatio="cover"
        facingMode='environment'
        className = "image-size"
      />
      )}

    <Control>
        <ImagePreview
          image={image}
          onClick={() => {
            setShowImage(!showImage);
          }}
        />
        <TakePhotoButton
          onClick={() => {
            if (camera.current) {
              const photo = camera.current.takePhoto();
              console.log(photo);
              setImage(photo);
            }
          }}
        />
        <ChangeFacingCameraButton
          disabled={numberOfCameras <= 1}
          onClick={() => {
            if (camera.current) {
              const result = camera.current.switchCamera();
              console.log(result);
            }
          }}
        />
      </Control>
    </Wrapper>
  );
}

export default Component;