import React, { useState, useRef, useEffect } from "react";
import "./App.css";
import axios from 'axios';
import { Navigate, useNavigate } from "react-router";
const ZepetoAuto = () => {
    
}

function LoadingClick(){
    window.location.href = "/Loading"
}
function Loading3Click(){
    window.location.href = "/Loading3"
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
    const [previewyolo,setPreviewYolo] = useState(sessionStorage.getItem("image_yolo3"));

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
          alert("다 완료 했습니다!")
      })
      .catch(err => {
          console.warn(err);
          alert("문제가 발생")
      })
      
      LoadingClick();
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
                Loading3Click()}>
                snapchat으로 안내</button>

        </div>
    );
};

export default SelectPage;