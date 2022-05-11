import React, { useState, Component, useEffect } from 'react';
import ReactLoading from "react-loading";
import { Navigate, useNavigate } from "react-router";
import SelectPage from './SelectPage';
import "./App.css";
import axios from 'axios';

const Loading = () => {

    function SelectPageClick(){
        window.location.href = "/SelectPage"
      }

    const [isLoading, setIsLoading] = useState(true);
    useEffect(() => {
        setIsLoading(true)
       axios({}).then(function (response){
            console.log(response)
       });
    },[])

    /* axios.post(url, data, {
        // 주소와 formdata를 posting 한다
     })
     .then(res => { 
       //상태 출력
         console.warn(res);
     });*/


    return (
        <div>
            {
            isLoading == true ? 
            <div className='App-header2'>
                <h1>로딩중 입니다</h1>
            <ReactLoading   type="spin" color="#0000FF"
                height={667} width={375} />
                </div> : SelectPageClick()
            }
        </div>
    );
}

export default Loading;