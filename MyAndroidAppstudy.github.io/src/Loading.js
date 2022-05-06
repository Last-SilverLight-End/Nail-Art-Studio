import React, { useState, Component, useEffect } from 'react';
import ReactLoading from "react-loading";
import { Navigate, useNavigate } from "react-router";
import SelectPage from './SelectPage';



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
            <ReactLoading type="spin" color="#0000FF"
                height={100} width={50} /> : SelectPageClick()
            }
        </div>
    );
}

export default Loading;