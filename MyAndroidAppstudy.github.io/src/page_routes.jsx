// Import dependencies
import React, { useRef, useState, useEffect } from "react";
import {  BrowserRouter as Router,  Routes,  Route} from "react-router-dom";


import App from "./App";
import About from "./About";
import Users from "./Users";
import Home from "./Home";
import Camera from "./Camera";
import Loading from "./Loading";
import Loading2 from "./Loading2";
import Loading3 from "./Loading3";
import Loginpage from "./Loginpage";
import SelectPage from "./SelectPage";
import Notfound from "./Notfound";
import finishPage_zepeto from "./finishPage_zepeto";
import YoloPage from "./YoloPage";
import Rotate_image from "./Rotate_image"
function Buttons() {
    return (
        <Router>
            <Routes>
                
                <Route path="/" element={<Home/>}/>
                <Route path="/Rotate_image" element={<Rotate_image/>}/>
                <Route path ="/App" element= {<App/>}/>
                <Route path ="/About"element= {<About/>}/>
                <Route path ="/Users" element={<Users/>}/>
                <Route path ="/Camera" element={<Camera/>}/>
                <Route path ="/Loading" element={<Loading/>}/>
                <Route path ="/Loading2" element={<Loading2/>}/>
                <Route path ="/Loading3" element={<Loading3/>}/>
                <Route path ="/Loginpage" element={<Loginpage/>}/>
                <Route path ="/finishPage_zepeto" element={<finishPage_zepeto/>}/>
                <Route path ="/SelectPage" element={<SelectPage/>}/>
                <Route path="*" element={<Notfound/>} />
                <Route path= "/YoloPage" element= {<YoloPage/>}/>

            </Routes>
        </Router>
    );
};

export default Buttons;