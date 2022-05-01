import React, { useState, useRef } from "react";
import {Camera} from "react-camera-pro";
import * as cocossd from "@tensorflow-models/coco-ssd";
import "./App.css";
const Component = () => {

    const camera = useRef(null);
    const [numberOfCameras, setNumberOfCameras] = useState(0);
    const [image, setImage] = useState(null);


  return (
    <div>
      <Camera ref={camera} numberOfCamerasCallback={setNumberOfCameras} />
      
      <img src={image} alt='이미지 미리보기' />
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
    </div>
  );
}

export default Component;