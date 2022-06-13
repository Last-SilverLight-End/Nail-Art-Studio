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
    const [next,setNext] = useState(false);
    const [input,setinput] = useState("");
    const [bytestring,setbytestring] = useState('');
    const [image,setimage] = useState('');
    const [file, setFile] = useState(dataURLtoFile(sessionStorage.getItem("image"), "anonymous.png"));
    const [file2, setFile2] = useState(dataURLtoFile(sessionStorage.getItem("image"), "anonymous.png"));
    const [previewfile, setPreviewFile] = useState(sessionStorage.getItem("image"));
    const [previewfile2, setPreviewFile2] = useState(sessionStorage.getItem("image"));
    const [gotonextcheck, setGoToNextCheck] = useState(true);
    const [savebase64data, setSaveBase64Data] = useState("");

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

    const upLoad = async () => {
        
        console.warn("upload")
        console.log(file.name);
        console.log(file2.name);
        let directory_file = "./"

        console.log(file)
        const formData = new FormData();
        formData.append('file',file)
        let url = "/detectObject";
        let route = file2.name;
        console.log(route);
        formData.append('route',route);

        function SelectPageClick(e){
            window.location.href = "/SelectPage"
          }
         // console.log(previewfile);
          
        axios.post(url,formData,{
        }).then(res => {
            console.log(res.data);
            if(res.data == "error occured")
            {
                console.log("not good")
                setGoToNextCheck(false);
                setPreviewFile(loadingYoloImages)
                
            }
            else{
                console.log("good")
                setGoToNextCheck(true);
                const bytestring = res.data.status.split('\'')[1];
                setPreviewFile(`data:image/png;base64,${bytestring}`);
                //console.log(previewfile);
                setNext(true);
            }
           
            
        
        }).catch(err => {
            console.log("upload error" , err);
            setNext(false);
        })

       // upLoad2();
    }

    const gotoNext = async () => {
        //console.log(file);

        const formData = new FormData();
        formData.append('file',file2);

        let url0 = "/uploader"
        axios.post(url0, formData, {
            // 주소와 formdata를 posting 한다
          })
            .then(res => {
              //상태 출력
              console.warn(res);
            }).catch(err => {
              console.log(err);
            });


        console.log(file2)
        let route = file2.name;
        console.log(route);
        formData.append('route',route);
        let url = "/cropping"

        axios.post(url,formData,{
        }).then(res => {
            console.log(res.data);
            if(res.data == "error occured")
            {
                console.log("not good")
                setGoToNextCheck(false);
                setPreviewFile(loadingYoloImages);
                alert("잘못 되었습니다 다시 찍어주세요!")
            }
            else{
                console.log("good")
                setGoToNextCheck(true);
            }
           
        
        }).catch(err => {
            console.log("upload error" , err);
            alert("잘못 되었습니다 다시 찍어주세요!")
            setGoToNextCheck(false);
        })
        
        setTimeout(() => {

            
            if(typeof window !== "undefined"){
                console.log("gogo");
                console.log(gotonextcheck);
                if(gotonextcheck == true)
                {
                    window.sessionStorage.setItem("image_yolo3", previewfile);
                    window.sessionStorage.setItem("image_name",file2.name)
                    window.location.href = "/Rotate_image";
                    // crop 과 merge 해서 보여주는 코드
                   // setPreviewFile("http://localhost:5000/bringimg")
                    //setPreviewFile(require("./../image/nft_image.png"))  
                }
                else{
                    alert("이미지가 좋지 않습니다 다른 이미지로 시도해 주세요!")
                }
            }
        }, 2000);
    
    }

    return (
        <div className='App'>
            <header className='App-header'>
                <p>
                    손이 제대로 인식 되었는지 확인하세요!
                </p>

                <div className="pre_img">
                {gotonextcheck ? <img src={previewfile} /> : <img src = {loadingYoloImages}/>}
               
                </div>

                <form >
                    <input id="imageinput"  type="file" name="image" onChange={ handleInputChange }  />
                </form>
                <button name="send" className="rotatebuttonLeft" id="sendbutton" onClick = {() => upLoad()}>Send</button>
               {/*  <button name="send2" id="sendbutton2" onClick = {() => upLoad2()}>Send2</button> */}
               <button name = "next" className="rotatebuttonLeft" id = "gotonext" onClick = {() => gotoNext()}>go to Next</button>
            </header>
        </div>
    );
}



export default YoloPage;