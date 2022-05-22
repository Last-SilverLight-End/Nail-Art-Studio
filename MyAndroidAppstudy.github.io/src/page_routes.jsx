// Import dependencies
import React, { useRef, useState, useEffect } from "react";
import {  BrowserRouter as Router,  Routes,  Route} from "react-router-dom";


import App from "./App";
import About from "./About";
import Users from "./Users";
import Home from "./Home";
import Camera from "./Camera";
import Loading from "./Loading";
import Loginpage from "./Loginpage";
import SelectPage from "./SelectPage";
import Notfound from "./Notfound";
import finishPage_zepeto from "./finishPage_zepeto";

function Buttons() {
    return (
        <Router>
            <Routes>
                
                <Route path="/" element={<Home/>}/>
                
                <Route path ="/App" element= {<App/>}/>
                <Route path ="/About"element= {<About/>}/>
                <Route path ="/Users" element={<Users/>}/>
                <Route path ="/Camera" element={<Camera/>}/>
                <Route path ="/Loading" element={<Loading/>}/>
                <Route path ="/Loginpage" element={<Loginpage/>}/>
                <Route path ="/finishPage_zepeto" element={<finishPage_zepeto/>}/>
                <Route path ="/SelectPage" element={<SelectPage/>}/>
                <Route path="*" element={<Notfound/>} />

            </Routes>
        </Router>
    );
};

export default Buttons;