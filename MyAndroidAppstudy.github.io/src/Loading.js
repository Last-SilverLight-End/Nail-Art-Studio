import React, { useState, Component, useEffect } from 'react';
import ReactLoading from "react-loading";
import { Navigate, useNavigate } from "react-router";
import SelectPage from './SelectPage';
import "./App.css";


const Loading = () => {

    function SelectPageClick(){
        window.location.href = "/SelectPage"
      }

    const [isLoading, setIsLoading] = useState(true);
    useEffect(() => {
        setTimeout(() => {
            setIsLoading(false);
        }, 3000);
    })
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