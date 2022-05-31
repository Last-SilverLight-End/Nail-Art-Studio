import React, { useState, useRef, useEffect } from "react";
import "./App.css";
import axios from 'axios';
import { Navigate, useNavigate } from "react-router";
const ZepetoAuto = () => {
    
}

const GuideZepeto = () => 
{
    axios.get('/rendering',
      )
      .then(res => { 
        //상태 출력
          console.warn(res);
      })
      .catch(err => {
          console.warn(err);
      })
}

const SelectPage = () => {
    const [image, setShowImage] = useState('');
    const [values, setValues] = useState({ id: "", password: "" });
    const [submitting, setSubmitting] = useState(false);
    const [errors, setErrors] = useState({});
    const [previewyolo,setPreviewYolo] = useState(sessionStorage.getItem("image_yolo2"));

    const handleChange = (event) => {
        const { name, value } = event.target;
        setValues({ ...values, [name]: value });
      };
    
    const handleSubmit = (event) => {
        event.preventDefault();
        setSubmitting(true);      
       
    if (values.id !="" && values.password.length >= 8) {
      alert("로그인 성공");
      // 여기에 fetch 넣고 적용
      const formdata = new FormData();

      formdata.append("data" ,values.id);
      formdata.append("pwd" , values.password);

      console.log(values.id);
      console.log(values.password);
     axios.post('/changeZepetoInfo',formdata,
     )
      .then(res => { 
        //상태 출력
          console.warn(res);
      })
      .catch(err => {
          console.warn(err);
      })
      GuideZepeto()
    }
    else
    {
        alert("다시 입력해 주세요");
        setSubmitting(false);
    }


    }
    return (
        <div className="App-header">
            <h1 > 사진 미리보기 </h1>
            <div className="pre_img">
                <img src={previewyolo} />   
            </div>
            <h1>Zepeto</h1>
            <form onSubmit= {handleSubmit}>
                <p>ID</p>
                <input
                value = {values.id} 
                name = "id" 
                onChange={handleChange}/>
                <p> Password</p>
                <input
                value = {values.password}
                name = "password"
                onChange = {handleChange}
                />

            <button type="submit" disabled= {submitting} className="buttonshow">
                Zepeto로 안내</button>
            </form>

            <h1>SnapChat</h1>

       
            
                <button className="buttonshow" onClick={() =>
                window.open('https://accounts.snapchat.com/accounts/login?continue=%2Faccounts%2Fwelcome', '_blank')}>
                snapchat으로 안내</button>

            <h1>NFT</h1>

       
            
                <button className="buttonshow" onClick={() =>
                window.open('https://accounts.snapchat.com/accounts/login?continue=%2Faccounts%2Fwelcome', '_blank')}>
                NFT로 안내</button>

        </div>
    );
};

export default SelectPage;