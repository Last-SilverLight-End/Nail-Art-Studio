import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import './index.css';
import App from "./App";
import Users from "./Users"
import Loginpage from './Loginpage';
import Looding from "./Loading"
import Page_routes from './page_routes';

ReactDOM.render(

    <Page_routes/>,
  document.getElementById('root')
);