import React, { useState, useRef } from "react";
import {Camera} from "react-camera-pro";
import "./App.css";
import Upload from "./Users";

function imageUploadFiles() {

  const saveFileImage = (e) => {
    Component.setFileImage(URL.createObjectURL(e.target.files[0]));
  };
  const deleteFileImage = () => {
    URL.revokeObjectURL(Component.fileImage);
    Component.setFileImage("");
  };
}

const Component = () => {

    const camera = useRef(null);
    const [numberOfCameras, setNumberOfCameras] = useState(0);
    const [image, setImage] = useState(null);
    const [fileimage, imageURL] = useState("");
    const [fileImage, setFileImage] = useState("");
  return (
    
    <div>
       <Camera ref={camera} 
       numberOfCamerasCallback={setNumberOfCameras} 
       aspectRatio={16 / 9} 
       facingMode='environment'/>
      
      <img src={image} alt='이미지 미리보기' />
      <button
        onClick={() => {
            const photo = camera.current.takePhoto();
            setImage(photo);
        }}
      > 카메라 사진 찍기
      </button>
      <form onSubmit={Upload.handleUploadImage}>
        <button
          onClick={() => {
            
        }}
        > 올리기
        </button>
      </form>
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