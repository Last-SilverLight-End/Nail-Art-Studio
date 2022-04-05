// Import dependencies
import React, { useRef, useState, useEffect } from "react";
import {  BrowserRouter as Router,  Routes,  Route} from "react-router-dom";
import App from "./App";
import About from "./About";
import Users from "./Users";
import Home from "./Home";
import Camera from "./Camera";
function Buttons() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home/>}/>
                <Route path ="/App" element= {<App/>}/>
                <Route path ="/About"element= {<About/>}/>
                <Route path ="/Users" element={<Users/>}/>
                <Route path ="/Camera" element={<Camera/>}/>
            </Routes>
        </Router>
    );
};

export default Buttons;