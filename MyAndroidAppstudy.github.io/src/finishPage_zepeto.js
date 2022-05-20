import React, { useState, useRef, useEffect } from "react";

const GuideZepeto = () => 
{
    window.open('https://studio.zepeto.me/kr/console/auth/signin', '_blank')
}

const finishPage_zepeto = () => {

    return (
        <div className="App-header">
            <h1 > 업로드가 끝났습니다! </h1>                         
            <button onClick={() => GuideZepeto()} className="buttonshow">
                Zepeto로 안내</button>
            <h1>SnapChat</h1>
                <button className="buttonshow" onClick={() =>
                window.open('https://accounts.snapchat.com/accounts/login?continue=%2Faccounts%2Fwelcome', '_blank')}>
                snapchat으로 안내</button>
        </div>
    );
};

export default finishPage_zepeto;