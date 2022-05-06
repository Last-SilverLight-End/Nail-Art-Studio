import React, { useState, Component, useEffect } from 'react';
import ReactLoading from "react-loading";
import { Navigate, useNavigate } from "react-router";
import SelectPage from './SelectPage';
const Loading = () => {
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
                height={100} width={50} /> : <SelectPage/>
            }
        </div>
    );
}

export default Loading;