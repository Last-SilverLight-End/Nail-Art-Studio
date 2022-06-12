import React, { useState, useRef, useEffect } from "react";
import { Camera } from "react-camera-pro";
import "./App.css";
import axios from 'axios';
import * as tf from "@tensorflow/tfjs";
import { Navigate, useNavigate } from "react-router";
import * as tmImage from '@teachablemachine/image';
//import { model } from "@tensorflow/tfjs";
import Resizer from "react-image-file-resizer";
import Modal from "./Modal";
import styled from "styled-components";
import asdf from "./Loginpage"

import tempimage from "./showExampleImg.png"
import finishPage_zepeto from "finishPage_zepeto";

const Wrapper = styled.div`
  background-position: center;
  
  width: 70%;
  height: 70%;
  left:0px;
  right:0px;
  margin: auto 0;
  margin-top: 2rem;
  margin-bottom :2rem;
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

const Component = () => {

  const camera = useRef(null);
  const [numberOfCameras, setNumberOfCameras] = useState(0);
  const [selectedFile, setSelectedFile] = useState('');
  const [image, setImage] = useState(tempimage);
  const navigate = useNavigate();
  const [showImage, setShowImage] = useState(false);
  const [showResult, setShowResult] = useState(false);
  const [Check, setCheck] = useState(false);
  const [Check2, setCheck2] = useState(false);
  const canvasRef = useRef(null);
  const [modalOpen, setModalOpen] = useState(true);
  const [readyModalOpen, setReadyModalOpen] = useState(false);
  const [readyModalOpen2, setReadyModalOpen2] = useState(false);

  const openModal = () => {
    setModalOpen(true);
  };
  const closeModal = () => {
    setModalOpen(false);
  }; 
  const readyCloseModal = () => {
    setReadyModalOpen(false);
  }
  const readyCloseModal2 = () => {
    setReadyModalOpen2(false);
  }
  //const [photo,setPhoto] = useState('');

  // teachable machine 모텔 불러오기 코드
  const URL = "https://teachablemachine.withgoogle.com/models/7TVFokN0L/";
  const modelURL = URL + "model.json";
  const metadataURL = URL + "metadata.json";
  const [predictionArr, setPredictionArr] = useState([]);
  let maxPredictions;
  let model;
  let imagenametemp;
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
        416,
        416,
        "PNG",
        122,
        0,
        (uri) => {
          resolve(uri);
        },
        "base64"
      );
    });


  async function init() {
    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();

  }



  async function predict() {


    setCheck2(false);
    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();



    // image png 화 시킨 후 -> predict 에 바로 들어갈수 있는지? or  base64 형태로 들어가는지?


    const tempImg = document.getElementById('srcImg');
    const prediction = await model.predict(tempImg, false);

    for (let i = 0; i < maxPredictions; i++) {
      const classPrediction = prediction[i].probability;
      console.log(prediction[i].className + ": " + classPrediction);
      //console.log(prediction[i].probability);
    }
    
    
    if (prediction[0].probability >= 0.0) {
      setCheck(true);
      
      // alert("준비 되었습니다! 업로드 하시려면 버튼을 눌러주세요!")
      //submit();
      setReadyModalOpen(true);
    }
    else {
      setCheck(false);

      //alert("다시 찍어 주세요");
      setReadyModalOpen2(true);
    }
    setCheck2(true);
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

  const submit = async () => {
    if (Check == true) {
      // 먼저 파일 변환 후에 
      console.log(image);
      const convertedFile = dataURLtoFile(image, "anonymous" + ".png");
      console.warn(convertedFile);

      //파일 사이즈 조절
      const file = convertedFile;
      const imagetemp = await resizeFile(file);
      console.log(imagetemp);

      const newFile = dataURLtoFile(imagetemp, "tempo" + ".png");
      

     if(typeof window !== "undefined"){
        window.sessionStorage.setItem("image", imagetemp);
        //window.sessionStoarage.setItem("imageName",imagetemp.name)
       // window.location.href = "/YoloPage";
      }


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
        }).catch(err => {
          console.log(err);
        });


      setTimeout(() => {
       // navigate('/Loading');
       navigate('/YoloPage');
      }, 2000);
    }
    else {
      if(Check2 == false)
      alert("잠시만 기다려 주세요!")
      else if(Check == false)
      alert("잘못된 사진 입니다 다시 찍어 주세요!")
    }
  }
  console.log(readyModalOpen);

  return (

    <div>
      {showImage ? (

        <div className="App-header3">
          {readyModalOpen && <Modal open close={readyCloseModal} header= "완료 되었습니다!">
            준비 되었습니다! 업로드 하시려면 버튼을 눌러주세요!
          </Modal>}
          {readyModalOpen2 && <Modal open close={readyCloseModal2} header= "완료 되었습니다!">
          사진이 정확하지 않습니다 다시 찍어 주세요!
          </Modal>}
          <Wrapper>
            <img id="srcImg"
              className="temp" src={image} alt='이미지 미리보기'>
            </img>
          </Wrapper>
          <button type="submit" className="buttonshow_camera2"
            onClick={() => submit()}> 업로드</button>
          <button type="submit" className="buttonshow_camera2"
            onClick={() => setShowImage(false)}> 다시 찍기</button>

        </div>

      ) : (
        <div className="App-header3">
          <Modal open={modalOpen} close={closeModal} header= "사진 찍는 방법">
          이런 형식으로 찍어주세요!
            <img  style={{ width: "100%", height: "100%x" }} src = {tempimage}></img>
          </Modal>
          <Wrapper>
            <Camera ref={camera} className="temp"
              numberOfCamerasCallback={setNumberOfCameras}
              aspectRatio={1 / 1}
              facingMode='environment'
              errorMessages={{
                noCameraAccessible: 'No camera device accessible. Please connect your camera or try a different browser.',
                permissionDenied: 'Permission denied. Please refresh and give camera permission.',
                switchCamera:
                  'It is not possible to switch camera to different one because there is only one video device accessible.',
                canvas: 'Canvas is not supported.',
              }}
            />
          </Wrapper>


          <button className="buttonshow_camera"
            onClick={() => {
              const photo = (camera.current.takePhoto());
              setImage(photo);
              setShowImage(true);
              predict();

            }}

          > 사진 찍기</button>

          <button className="buttonshow_camera"
            hidden={numberOfCameras <= 1}
            onClick={() => {
              const photo = (camera.current.switchCamera());
              setImage(photo);
              predict();
            }}
          >카메라 전환 </button>

        </div>
      )
      }
    </div>

  );
}

export default Component;