import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navigation from "./components/Navigation";
import Home from "./components/Home";
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Devices from "./components/Devices";
import Manage from "./components/Manage";

function App() {
  return (
  <BrowserRouter>
    <Navigation />
    <Routes>
         <Route exact path="/" element={<Home/>} />
         <Route path="/report" element={<Devices/>} />
         <Route path="/manage" element={<Manage/>} />

       </Routes>
  </BrowserRouter>
  );
}

export default App;