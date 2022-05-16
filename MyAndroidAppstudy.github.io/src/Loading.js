import React, { useState, Component, useEffect } from 'react';
import ReactLoading from "react-loading";
import { Navigate, useNavigate } from "react-router";
import SelectPage from './SelectPage';
import "./App.css";
import axios from 'axios';
import Camera from './Camera';
const Loading = () => {

    function SelectPageClick(){
        window.location.href = "/SelectPage"
    }
    function CameraClick(){
        window.location.href = "/Camera"
    }
    const [isLoading, setIsLoading] = useState(true);
    useEffect(() => {
        setIsLoading(true)
       axios("/rendering",{}).then(res => {
            console.warn(res)
            SelectPageClick()
       }).catch(res => {
           console.warn(res +  "error must be fix!")
           CameraClick()
       })
    },[])



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