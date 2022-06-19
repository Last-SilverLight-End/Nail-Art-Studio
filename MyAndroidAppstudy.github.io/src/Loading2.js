import React, { useState, Component, useEffect } from 'react';
import ReactLoading from "react-loading";
import { Navigate, useNavigate } from "react-router";
import SelectPage from './SelectPage';
import "./App.css";
import axios from 'axios';
import Camera from './Camera';

// nft 이야기
const Loading2 = () => {

    function SelectPageClick(){
        window.location.href = "/SelectPage"
    }
    function CameraClick(){
        window.location.href = "/Camera"
    }
    function YoloClick(){
        window.location.href = "/YoloPage"
    }
    const [isLoading, setIsLoading] = useState(true);
    useEffect(() => {
        setIsLoading(true)
       axios("/rendering2",{}).then(res => {
            console.warn(res.data)
           // if(res.data = "error occured")
           // alert("제대로 올리지 못했습니다 다시 시도해 주세요")
           // else
            alert("다 끝났습니다 확인해 주세요!")
            SelectPageClick()
       }).catch(res => {
           console.warn(res +  "error must be fix!")
           alert("문제 발생! yolo로 되돌아 갑니다")
           YoloClick()
       })
    },[])

    /*useEffect(() => {
        setTimeout(() => {
            alert("다 끝났습니다 확인해 주세요!")
            SelectPageClick()
        }, 3000);
    },[])*/



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

export default Loading2;