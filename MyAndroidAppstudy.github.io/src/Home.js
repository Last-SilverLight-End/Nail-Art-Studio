import React,{useState,useEffect} from "react";
import "./App.css";


const Home = () => {

  function AboutClick(e){
    window.location.href = "/About"
  }
  function CameraClick(e){
    window.location.href = "/Camera"
  }function  UserClick(e){
    window.location.href = "/Users"
  }
  function DataClick(e){
    window.location.herf = "/Data"
  }
  useEffect(()=> {
    fetch('/api',{mode : "no-cors"}).then(response => {
      if(response.ok){
        return response.json()
      }
    }).then(data => console.log(data))
  })

    return (
      <div className="App">
      <header className="App-header">
        <h1>안녕하세요!</h1>
        <p>NailStudio에 오신걸 환영합니다!</p>
        <button className="buttontransfer"
         onClick = {DataClick}>NailStudio 소개</button>
         <button className="buttontransfer"
         onClick = {CameraClick}> 사진 찍기 </button>
         <button className="buttontransfer"
         onClick = {UserClick}> 사용자 정보 </button>
        </header>
      </div>
    );
  };

  export default Home;