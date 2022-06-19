import React, { useState, Component, useEffect } from 'react';
import ReactLoading from "react-loading";
import { Navigate, useNavigate } from "react-router";
import SelectPage from './SelectPage';
import "./App.css";
import axios from 'axios';
import Camera from './Camera';

// snap-chat 자동 진행
const Loading3 = () => {
    
    function SelectPageClick() {
        window.location.href = "/SelectPage"
    }
    function CameraClick() {
        window.location.href = "/Camera"
    }
    const [snapchatemail,setSnapChatEmail] = useState(sessionStorage.getItem("snapvalues"));
    const [isLoading, setIsLoading] = useState(true);
    useEffect(() => {
        setIsLoading(true)
        let formdata = new FormData;
        formdata.append("val",snapchatemail);
        console.log(snapchatemail);
        axios.post("/method", {}).then(res => {
            console.warn(res.data)
            // if(res.data = "error occured")
            // alert("제대로 올리지 못했습니다 다시 시도해 주세요")
            // else
            console.log(res.data);
            //console.log(snapchatemail); // 잘 받아와지는거 확인
            if (res.data == "error occured") {
                alert("하는 도중 오류가 발생하였습니다!");
                SelectPageClick();
            }
            else {
                let temp2 = "다 끝났습니다! " + res.data + " 으로 접속해주세요! ";
                window.sessionStorage.setItem("snapchat", res.data);
                alert(temp2);
                SelectPageClick();
            }
        }).catch(res => {
            console.warn(res + "error must be fix!");
            alert("문제 발생! 선택 페이지로 되돌아갑니다");
            SelectPageClick();
        })
    }, []);

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
                        <ReactLoading type="spin" color="#0000FF"
                            height={667} width={375} />
                    </div> : SelectPageClick()
            }
        </div>
    );
}

export default Loading3;